import pytest

from .loader import TitsaError, User


def test_create_user(db, user):
    db.cur.execute('SELECT * FROM users WHERE id = :id', {'id': user.id})
    result = db.cur.fetchone()
    assert result is not None
    assert result['id'] == user.id
    assert result['name'] == user.name
    assert result['credit'] == user.credit


def test_get_user(user):
    user = User(user.id)
    assert user is not None


def test_create_user_fails_when_id_has_wrong_format():
    with pytest.raises(TitsaError) as exc:
        User('invalid_id', 'Guido van Rossum', 100)
    assert str(exc.value) == 'Invalid user ID format: invalid_id'


def test_get_name(db, user):
    db.cur.execute('SELECT * FROM users WHERE id = :id', {'id': user.id})
    result = db.cur.fetchone()
    assert result is not None
    assert user.name == result['name'] == 'Guido van Rossum'


def test_get_name_when_user_does_not_exist(db):
    user = User('12345678A', 'Nonexistent User', 0)
    db.cur.execute(
        'DELETE FROM users WHERE id = :id', {'id': user.id}
    )  # Ensure the user does not exist
    assert user.name == ''


def test_set_name(db, user):
    user.name = 'New Name'
    db.cur.execute('SELECT * FROM users WHERE id = :id', {'id': user.id})
    result = db.cur.fetchone()
    assert result is not None
    assert user.name == result['name'] == 'New Name'


def test_get_credit(db, user):
    db.cur.execute('SELECT * FROM users WHERE id = :id', {'id': user.id})
    result = db.cur.fetchone()
    assert result is not None
    assert user.credit == result['credit'] == 100


def test_get_credit_when_user_does_not_exist(db):
    user = User('12345678A', 'Nonexistent User', 0)
    db.cur.execute(
        'DELETE FROM users WHERE id = :id', {'id': user.id}
    )  # Ensure the user does not exist
    assert user.credit == 0


def test_set_credit(db, user):
    user.credit = 150
    db.cur.execute('SELECT * FROM users WHERE id = :id', {'id': user.id})
    result = db.cur.fetchone()
    assert result is not None
    assert user.credit == result['credit'] == 150
