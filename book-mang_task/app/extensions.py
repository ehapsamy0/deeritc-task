from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
import logging
from flask_migrate import Migrate


# Initialize the extensions
db = SQLAlchemy()
jwt = JWTManager()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
migrate = Migrate()