import factory
from werkzeug.security import generate_password_hash
from app.models.user import User
from app.extensions import db

class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = db.session  # This connects the factory to the db session

    id = factory.Sequence(lambda n: n + 1)  # Sequential IDs
    email = factory.LazyAttribute(lambda obj: f"{obj.username}@example.com")
    username = factory.Faker("user_name")
    password_hash = factory.LazyAttribute(lambda x: generate_password_hash("password123"))  # Default hashed password
