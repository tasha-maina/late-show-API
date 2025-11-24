import pytest
import sys
import werkzeug

# FIX WERKZEUG BUG
if not hasattr(werkzeug, "__version__"):
    werkzeug.__version__ = "0.0"

# allow imports from server/
sys.path.append("..")

from app import create_app
from models import db as _db


@pytest.fixture()
def app():
    """Create a new app and database for EACH test."""
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    with app.app_context():
        _db.create_all()
        yield app
        _db.session.remove()
        _db.drop_all()


@pytest.fixture()
def client(app):
    """Flask test client."""
    return app.test_client()


@pytest.fixture()
def db(app):
    """Database instance."""
    return _db
