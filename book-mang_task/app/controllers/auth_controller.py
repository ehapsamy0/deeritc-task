from flask import request
from flask_restx import Namespace, Resource, fields
from app.services.auth_service import register_user, login_user
from app.extensions import db, logger
# Create a namespace for auth routes
auth_ns = Namespace('auth', description='Authentication related operations')

user_model = auth_ns.model('User', {
    'username': fields.String(required=True, description='The user username'),
    'email': fields.String(required=True, description='The user email address'),
    'password': fields.String(required=True, description='The user password'),
    'phone': fields.String(required=False, max_length=20, description='The user phone number'),
})

login_model = auth_ns.model('Login', {
    'email': fields.String(required=True, description='The user email address'),
    'password': fields.String(required=True, description='The user password')
})

@auth_ns.route('/register')
class Register(Resource):
    @auth_ns.expect(user_model)
    def post(self):
        """Register a new user"""
        data = request.json
        data['email'] = data['email'].strip().lower()
        data['username'] = data['username'].strip()

        if not data or not isinstance(data, dict):
            logger.warning("Invalid input format for registration.")
            return {"error": "Invalid input format"}, 400


        return register_user(request.json)

@auth_ns.route('/login')
class Login(Resource):
    @auth_ns.expect(login_model)
    def post(self):
        """Login a user and return a token"""
        data = request.json
        if not data or not isinstance(data, dict):
            logger.warning("Invalid input format for login.")
            return {"error": "Invalid input format"}, 400
        data['email'] = data['email'].strip().lower()
        return login_user(request.json)
