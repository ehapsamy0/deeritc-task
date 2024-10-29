from app.extensions import db
from sqlalchemy import func

class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    description = db.Column(db.Text, nullable=True)
    published_date = db.Column(db.Date, nullable=False, server_default=db.func.current_date())
    pages = db.Column(db.Integer, nullable=True)
    isbn = db.Column(db.String(13), nullable=True)
    # Relationships
    author = db.relationship('User', back_populates='books')
    bookings = db.relationship('Booking', back_populates='book', cascade="all, delete-orphan")


    def __repr__(self):
        return f"<Book {self.title} by {self.author}>"



