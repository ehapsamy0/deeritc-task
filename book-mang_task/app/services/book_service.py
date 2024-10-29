from app.models.book import Book
from app.models.booking import Booking
from app.extensions import db, logger
from datetime import datetime
from sqlalchemy.orm import joinedload
from app.models.user import User


def validate_book_data(data):
    """Validates book data for minimum requirements."""
    if not data.get("title"):
        return "Title is required"
    if len(data.get("title")) < 3:
        return "Title must be at least 3 characters long"
    return None


def validate_booking_data(booking_data):
    """Validates booking data for minimum requirements."""
    if not booking_data.get("customer_name"):
        return "Customer name is required"
    if not booking_data.get("customer_contact"):
        return "Customer contact is required"
    if not booking_data.get("start_date") or not booking_data.get("end_date"):
        return "Both start and end dates are required"

    # Validate date format and that dates are logical
    try:
        today = datetime.today().date()
        start_date = datetime.strptime(booking_data["start_date"], "%Y-%m-%d").date()
        end_date = datetime.strptime(booking_data["end_date"], "%Y-%m-%d").date()

        if start_date < today:
            return "Start date cannot be before today"
        if start_date > end_date:
            return "End date must be after the start date"
    except ValueError:
        return "Invalid date format; please use YYYY-MM-DD"

    return None


def create_book(data):
    title = data.get("title")
    description = data.get("description")
    author_id = data.get("author_id")
    isbn = data.get("isbn", None)
    published_date = data.get("published_date", None)
    pages = data.get("pages", 0)

    if not author_id:
        logger.warning("author_id is required.")
        return {"error": "author_id is required"}, 400

    author = User.query.get(author_id)
    if not author:
        logger.warning("Author not found with ID: %s", author_id)
        return {"error": "Author not found"}, 404

    new_book = Book(
        title=title,
        description=description,
        author_id=author_id,
        isbn=isbn,
        published_date=published_date,
        pages=pages,
    )

    try:
        db.session.add(new_book)
        db.session.commit()
        logger.info("Book created successfully with title: %s", title)

        return {
            "message": "Book created successfully.",
            "book": {
                "id": new_book.id,
                "title": new_book.title,
                "description": new_book.description,
                "author_id": new_book.author_id,
                "published_date": new_book.published_date.isoformat()
                if new_book.published_date
                else None,
                "isbn": new_book.isbn,
                "pages": new_book.pages,
            },
        }, 201
    except Exception as e:
        db.session.rollback()
        logger.error("Database error during book creation: %s", str(e))
        return {"error": "An error occurred while creating the book"}, 500


def get_books(page=1, per_page=10):
    logger.info(
        "Retrieving books with pagination: page %d, per_page %d", page, per_page
    )
    paginated_books = Book.query.options(joinedload(Book.author)).paginate(
        page=page, per_page=per_page, error_out=False
    )
    books = [
        {
            "id": book.id,
            "title": book.title,
            "description": book.description,
            "author": {
                "id": book.author.id,
                "username": book.author.username,
                "email": book.author.email,
                "phone": book.author.phone,
            },
        }
        for book in paginated_books.items
    ]

    return {
        "books": books,
        "total": paginated_books.total,
        "page": paginated_books.page,
        "pages": paginated_books.pages,
        "per_page": paginated_books.per_page,
    }, 200


def update_book(book_id, data):
    logger.info("Starting book update process for ID: %s", book_id)
    book = Book.query.get(book_id)
    if not book:
        logger.warning("Book not found for ID: %s", book_id)
        return {"error": "Book not found"}, 404

    # Update fields
    book.title = data.get("title", book.title)
    book.description = data.get("description", book.description)
    book.isbn = data.get("isbn", book.isbn)
    book.pages = data.get("pages", book.pages)

    try:
        db.session.commit()
        logger.info("Book updated successfully for ID: %s", book_id)
        return {"message": "Book updated successfully."}, 200
    except Exception as e:
        db.session.rollback()
        logger.error("Database error during book update: %s", str(e))
        return {"error": "An error occurred while updating the book"}, 500


def delete_book(book_id):
    logger.info("Starting book deletion process for ID: %s", book_id)
    book = Book.query.get(book_id)
    if not book:
        logger.warning("Book not found for ID: %s", book_id)
        return {"error": "Book not found"}, 404

    try:
        db.session.delete(book)
        db.session.commit()
        logger.info("Book deleted successfully for ID: %s", book_id)
        return {"message": "Book deleted successfully."}, 200
    except Exception as e:
        db.session.rollback()
        logger.error("Database error during book deletion: %s", str(e))
        return {"error": "An error occurred while deleting the book"}, 500


def book_booking(book_id, booking_data):
    logger.info("Starting booking process for book ID: %s", book_id)

    book = Book.query.get(book_id)
    if not book:
        logger.warning("Book not found for ID: %s", book_id)
        return {"error": "Book not found"}, 404

    validation_error = validate_booking_data(booking_data)
    if validation_error:
        logger.warning("Booking validation failed: %s", validation_error)
        return {"error": validation_error}, 400

    customer_name = booking_data.get("customer_name")
    customer_contact = booking_data.get("customer_contact")
    start_date = datetime.strptime(booking_data["start_date"], "%Y-%m-%d")
    end_date = datetime.strptime(booking_data["end_date"], "%Y-%m-%d")

    # Create booking entry
    booking = Booking(
        customer_name=customer_name,
        customer_contact=customer_contact,
        start_date=start_date,
        end_date=end_date,
        book_id=book_id,
    )

    try:
        db.session.add(booking)
        db.session.commit()
        logger.info("Booking created successfully for book ID: %s", book_id)
        return {
            "message": "Booking created successfully.",
            "booking": {
                "id": booking.id,
                "customer_name": booking.customer_name,
                "start_date": booking.start_date.strftime("%Y-%m-%d"),
                "end_date": booking.end_date.strftime("%Y-%m-%d"),
                "book_id": booking.book_id,
            },
        }, 201
    except Exception as e:
        db.session.rollback()
        logger.error("Database error during booking creation: %s", str(e))
        return {"error": "An error occurred while creating the booking"}, 500


def get_bookings(page=1, per_page=10):
    logger.info(
        "Retrieving bookings with pagination: page %d, per_page %d", page, per_page
    )
    paginated_bookings = Booking.query.options(
        joinedload(Booking.book).joinedload(Book.author)
    ).paginate(page=page, per_page=per_page, error_out=False)

    bookings = [
        {
            "id": booking.id,
            "customer_name": booking.customer_name,
            "customer_contact": booking.customer_contact,
            "start_date": booking.start_date.isoformat(),
            "end_date": booking.end_date.isoformat(),
            "book": {
                "id": booking.book.id,
                "title": booking.book.title,
                "author": {
                    "id": booking.book.author.id,
                    "username": booking.book.author.username,
                    "email": booking.book.author.email,
                    "phone": booking.book.author.phone,
                },
            },
        }
        for booking in paginated_bookings.items
    ]

    return {
        "bookings": bookings,
        "total": paginated_bookings.total,
        "page": paginated_bookings.page,
        "pages": paginated_bookings.pages,
        "per_page": paginated_bookings.per_page,
    }, 200

def get_bookings_for_book(book_id, page=1, per_page=10):
    """Retrieve all bookings for a specific book with pagination."""
    logger.info("Retrieving bookings for book ID %d with pagination: page %d, per_page %d", book_id, page, per_page)

    # Query paginated bookings for the specified book
    paginated_bookings = (
        Booking.query
        .filter_by(book_id=book_id)
        .options(joinedload(Booking.book).joinedload(Book.author))  # Load the author through the book relationship
        .paginate(page=page, per_page=per_page, error_out=False)
    )

    # Format booking data
    bookings = [
        {
            "id": booking.id,
            "customer_name": booking.customer_name,
            "customer_contact": booking.customer_contact,
            "start_date": booking.start_date.isoformat(),
            "end_date": booking.end_date.isoformat(),
            "book": {
                "id": booking.book.id,
                "title": booking.book.title,
                "author": {
                    "id": booking.book.author.id,
                    "username": booking.book.author.username,
                    "email": booking.book.author.email,
                    "phone": booking.book.author.phone,
                },
            },
        }
        for booking in paginated_bookings.items
    ]

    return {
        "bookings": bookings,
        "total": paginated_bookings.total,
        "page": paginated_bookings.page,
        "pages": paginated_bookings.pages,
        "per_page": paginated_bookings.per_page,
    }, 200
