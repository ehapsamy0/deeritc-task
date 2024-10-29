import factory
from app.models.book import Book
from app.extensions import db
from datetime import date
from tests.factories.user_factory import UserFactory

class BookFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Book
        sqlalchemy_session = db.session

    id = factory.Sequence(lambda n: n + 1)  # Sequential IDs
    title = factory.Faker("sentence", nb_words=4)
    description = factory.Faker("paragraph", nb_sentences=3)
    isbn = factory.Faker("isbn13")  # Uses the Faker library to generate an ISBN-13
    pages = factory.Faker("random_int", min=50, max=500)
    published_date = factory.LazyFunction(date.today)
    author = factory.SubFactory(UserFactory)  # Creates a related User instance as the author
