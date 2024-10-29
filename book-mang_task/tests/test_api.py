import uuid
import pytest
from tests.factories.book_factory import BookFactory
from tests.factories.user_factory import UserFactory

# Fixture to create a book to use in tests
@pytest.fixture
def create_book(client):
    author = UserFactory.create(username="test_author", email="author@example.com")
    response = client.post('/api/books/', json={
        'title': 'Test Book',
        'description': 'This is a test book description.',
        'author_id': author.id,
        'isbn': '1234567890123',
        'pages': 300
    })
    assert response.status_code == 201
    data = response.get_json()
    return data['book']['id']


def test_create_book(client, auth_header):
    author = UserFactory.create(username="test_author", email="author@example.com")
    response = client.post('/api/books/', json={
        'title': 'New Book',
        'description': 'Content of the new book.',
        'author_id': author.id,
        'isbn': '9876543210987',
        'pages': 200
    }, headers=auth_header)
    assert response.status_code == 201
    data = response.get_json()
    assert 'book' in data
    assert data['book']['title'] == 'New Book'


def test_update_book(client, create_book, auth_header):
    book_id = create_book
    response = client.put(f'/api/books/{book_id}', json={
        'title': 'Updated Title',
        'description': 'Updated description of the book.'
    }, headers=auth_header)  # Add the auth header here
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'Book updated successfully!'


def test_delete_book(client, create_book, auth_header):
    book_id = create_book
    response = client.delete(f'/api/books/{book_id}', headers=auth_header)  # Add the auth header here
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'Book deleted successfully!'