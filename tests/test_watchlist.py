"""
tests/test_watchlist.py — CineLog

Tests for the watchlist service, following the same patterns as
test_collection.py.
"""

import pytest
from app import create_app, db
from models import User, Film, WatchlistEntry
from services.watchlist_service import (
    add_to_watchlist,
    AlreadyInWatchlistError,
)
from services.collection_service import FilmNotFoundError


@pytest.fixture
def app():
    """Create an isolated test app with an in-memory database."""
    app = create_app(config={
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
    })
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def sample_user(app):
    """A user to use in tests."""
    with app.app_context():
        user = User(username="testuser", email="test@example.com")
        db.session.add(user)
        db.session.commit()
        return user.id


@pytest.fixture
def sample_film(app):
    """A film to use in tests."""
    with app.app_context():
        film = Film(title="Paddington 2", year=2017, genre="Comedy")
        db.session.add(film)
        db.session.commit()
        return film.id


# ── Basic add ───────────────────────────────────────────────────────────────

def test_add_to_watchlist_creates_entry(app, sample_user, sample_film):
    """
    Adding a valid film should create a WatchlistEntry in the database.
    """
    with app.app_context():
        entry = add_to_watchlist(user_id=sample_user, film_id=sample_film)

        assert entry is not None
        assert entry.user_id == sample_user
        assert entry.film_id == sample_film

        in_db = WatchlistEntry.query.filter_by(
            user_id=sample_user, film_id=sample_film
        ).first()
        assert in_db is not None


# ── Deduplication ────────────────────────────────────────────────────────────

def test_add_to_watchlist_duplicate_raises(app, sample_user, sample_film):
    """
    Adding the same film to the watchlist twice should raise
    AlreadyInWatchlistError, not silently create a duplicate entry.

    This is the critical test: WatchlistEntry has no unique DB constraint
    on (user_id, film_id), so the only thing preventing duplicates is the
    application-level check in add_to_watchlist(). Without this test, a
    regression here (e.g. someone removing the check) would go undetected
    until duplicates showed up in production.
    """
    with app.app_context():
        add_to_watchlist(user_id=sample_user, film_id=sample_film)

        with pytest.raises(AlreadyInWatchlistError):
            add_to_watchlist(user_id=sample_user, film_id=sample_film)

        # Confirm only one entry exists, not two
        count = WatchlistEntry.query.filter_by(
            user_id=sample_user, film_id=sample_film
        ).count()
        assert count == 1


def test_add_to_watchlist_duplicate_same_film_different_users_allowed(
    app, sample_film
):
    """
    Two different users should each be able to add the same film to their
    own watchlist — the dedup check is scoped to (user_id, film_id), not
    film_id alone.
    """
    with app.app_context():
        user_a = User(username="user_a", email="a@example.com")
        user_b = User(username="user_b", email="b@example.com")
        db.session.add_all([user_a, user_b])
        db.session.commit()

        entry_a = add_to_watchlist(user_id=user_a.id, film_id=sample_film)
        entry_b = add_to_watchlist(user_id=user_b.id, film_id=sample_film)

        assert entry_a.id != entry_b.id

        count = WatchlistEntry.query.filter_by(film_id=sample_film).count()
        assert count == 2