import pytest
from app import create_app
from app.extensions import db
from sqlalchemy import event
from sqlalchemy.orm import sessionmaker

from tests.factories.user_factory import UserFactory


import pytest
from app import create_app
from app.extensions import db
from tests.factories.user_factory import UserFactory
from flask_jwt_extended import create_access_token


@pytest.fixture(scope="session")
def app():
    app = create_app()
    app.config["TESTING"] = True
    with app.app_context():
        yield app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True

    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create tables
            yield client
            db.session.remove()
            db.drop_all()  # Clean up after each test


# Setting up the database session for tests
@pytest.fixture(scope="session")
def db_session(app):
    with app.app_context():
        db.create_all()
        yield db.session
        db.drop_all()
        db.session.remove()


@pytest.fixture
def create_book(client, db_session):
    # Setting up a temporary author
    author = UserFactory.create(username="test_author", email="author@example.com")
    db_session.add(author)
    db_session.commit()

    response = client.post(
        "/api/books/",
        json={
            "title": "Test Book",
            "description": "This is a test book description.",
            "author_id": author.id,
            "isbn": "1234567890123",
            "pages": 300,
        },
    )
    assert response.status_code == 201
    data = response.get_json()
    return data["book"]["id"]


@pytest.fixture
def auth_header(client):
    # Create a test user and get an auth token
    user = UserFactory.create(username="test_user", email="test_user@example.com")
    access_token = create_access_token(identity=user.id)
    return {"Authorization": f"Bearer {access_token}"}
