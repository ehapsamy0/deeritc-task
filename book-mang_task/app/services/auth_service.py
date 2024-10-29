import re
from app.models.user import User
from app.extensions import db, logger
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

EMAIL_REGEX = r"^[\w\.-]+@[\w\.-]+\.\w+$"

def validate_password(password):
    """Validates the password for minimum requirements."""
    if len(password) < 8:
        return "Password must be at least 8 characters long"
    if not re.search(r"[A-Z]", password):
        return "Password must contain at least one uppercase letter"
    if not re.search(r"[a-z]", password):
        return "Password must contain at least one lowercase letter"
    if not re.search(r"[0-9]", password):
        return "Password must contain at least one number"
    return None

def register_user(data):
    logger.info("Starting user registration process.")
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    phone = data.get("phone")

    if not (username and email and password):
        logger.warning("Missing required fields in registration.")
        return {"error": "Missing required fields: username, email, and password"}, 400

    if not re.match(EMAIL_REGEX, email):
        logger.warning("Invalid email format provided: %s", email)
        return {"error": "Invalid email format"}, 400

    if User.query.filter_by(username=username).first():
        logger.warning("Username already exists: %s", username)
        return {"error": "Username already exists"}, 409
    if User.query.filter_by(email=email).first():
        logger.warning("Email already exists: %s", email)
        return {"error": "Email already exists"}, 409

    password_error = validate_password(password)
    if password_error:
        logger.warning("Password validation failed.")
        return {"error": password_error}, 400

    hashed_password = generate_password_hash(password)
    new_user = User(username=username, email=email, password_hash=hashed_password, phone=phone)
    logger.warning(f"new_user {new_user.phone}.")

    try:
        db.session.add(new_user)
        db.session.commit()
        logger.info("User registered successfully: %s", username)
    except Exception as e:
        db.session.rollback()
        logger.error("Database error during user registration: %s", str(e))
        return {"error": "An error occurred while creating the user"}, 500

    return {
        "message": "User registered successfully.",
        "user": {
            "id": new_user.id,
            "username": new_user.username,
            "email": new_user.email,
            "phone": new_user.phone

        }
    }, 201






def login_user(data):
    logger.info("Starting user login process.")
    email = data.get("email")
    password = data.get("password")

    if not (email and password):
        logger.warning("Missing required fields in login.")
        return {"error": "Missing required fields: email and password"}, 400

    if not re.match(EMAIL_REGEX, email):
        logger.warning("Invalid email format provided: %s", email)
        return {"error": "Invalid email format"}, 400

    user = User.query.filter_by(email=email).first()
    
    if user and check_password_hash(user.password_hash, password):
        access_token = create_access_token(identity=user.id)
        logger.info("User logged in successfully: %s", email)
        return {
            "message": "Login successful",
            "access_token": access_token,
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "phone": user.phone
            }
        }, 200
    
    logger.warning("Invalid login attempt for email: %s", email)
    return {"error": "Invalid email or password"}, 401
