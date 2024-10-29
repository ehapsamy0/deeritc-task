from flask import request
from app.services.book_service import (
    create_book,
    get_bookings,
    get_bookings_for_book,
    get_books,
    update_book,
    delete_book,
    book_booking,
)
from flask_restx import Namespace, Resource, fields
from app.extensions import db, logger
from .auth_controller import user_model
from flask_jwt_extended import jwt_required, get_jwt_identity


book_ns = Namespace("books", description="Book operations")


book_response_model = book_ns.model(
    "Book",
    {
        "id": fields.Integer(description="The book ID"),
        "title": fields.String(required=True, description="The book title"),
        "description": fields.String(description="The book description"),
        "isbn": fields.String(description="The book isbn"),
        "pages": fields.Integer(required=True, description="The book page number"),
        "author": fields.Nested(user_model, description="Details of the book's author"),
    },
)

book_create_model = book_ns.model(
    "Book",
    {
        "title": fields.String(required=True, description="The book title"),
        "description": fields.String(description="The book description"),
        "isbn": fields.String(description="The book isbn"),
        "author_id": fields.Integer(required=True, description="The author's user ID"),
        "pages": fields.Integer(required=True, description="The book page number"),
    },
)

booking_model = book_ns.model(
    "Booking",
    {
        "customer_name": fields.String(
            required=True, description="Customer's full name"
        ),
        "customer_contact": fields.String(
            required=True, description="Customer's contact information"
        ),
        "start_date": fields.String(
            required=True, description="Booking start date in YYYY-MM-DD format"
        ),
        "end_date": fields.String(
            required=True, description="Booking end date in YYYY-MM-DD format"
        ),
    },
)


booking_response_model = book_ns.model(
    "BookingResponse",
    {
        "id": fields.Integer(description="The booking ID"),
        "customer_name": fields.String(description="The customer name"),
        "customer_contact": fields.String(
            description="The customer contact information"
        ),
        "start_date": fields.String(description="The booking start date"),
        "end_date": fields.String(description="The booking end date"),
        "book": fields.Nested(
            book_response_model, description="Details of the booked book"
        ),
    },
)


pagination_model = book_ns.model(
    "PaginatedBooks",
    {
        "books": fields.List(
            fields.Nested(book_response_model),
            description="List of books with pagination",
        ),
        "total": fields.Integer(description="Total number of books"),
        "page": fields.Integer(description="Current page number"),
        "pages": fields.Integer(description="Total number of pages"),
        "per_page": fields.Integer(description="Number of books per page"),
    },
)


@book_ns.route("/")
class BookList(Resource):
    @book_ns.doc(params={"page": "Page number", "per_page": "Number of books per page"})
    @book_ns.marshal_with(pagination_model)
    def get(self):
        """Get all books with pagination and author details"""
        page = request.args.get("page", default=1, type=int)
        per_page = request.args.get("per_page", default=10, type=int)
        books, status = get_books(page=page, per_page=per_page)
        return books, status
    
    @jwt_required()
    @book_ns.expect(book_create_model)
    @book_ns.doc(security="Bearer Auth")
    def post(self):
        """Create a new book"""
        data = request.json

        if not data or not isinstance(data, dict):
            logger.warning("Invalid input format for book creation.")
            return {"error": "Invalid input format"}, 400

        data["title"] = data["title"].strip()
        if "description" in data:
            data["description"] = data["description"].strip()

        return create_book(data)


# Book Detail route
@book_ns.route("/<int:book_id>")
class BookDetail(Resource):
    @jwt_required()
    @book_ns.doc(security="Bearer Auth")
    @book_ns.expect(book_create_model)
    def put(self, book_id):
        """Update a book by ID"""
        data = request.json
        data["title"] = data["title"].strip()
        if "description" in data:
            data["description"] = data["description"].strip()
        return update_book(book_id, data)

    @jwt_required()
    @book_ns.doc(security="Bearer Auth")
    def delete(self, book_id):
        """Delete a book by ID"""
        return delete_book(book_id)


@book_ns.route("/<int:book_id>/booking")
class BookBooking(Resource):


    @jwt_required()
    @book_ns.doc(security="Bearer Auth")
    @book_ns.doc(params={'page': 'Page number', 'per_page': 'Number of bookings per page'})
    def get(self, book_id):
        """Get all bookings for a specific book with pagination"""
        page = request.args.get('page', default=1, type=int)
        per_page = request.args.get('per_page', default=10, type=int)
        bookings, status = get_bookings_for_book(book_id, page=page, per_page=per_page)
        return bookings, status

    @jwt_required()
    @book_ns.doc(security="Bearer Auth")
    @book_ns.expect(booking_model)
    def post(self, book_id):
        """Create a booking for a book"""
        booking_data = request.json
        return book_booking(book_id, booking_data)

