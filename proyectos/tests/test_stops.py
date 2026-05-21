import pytest

from .loader import Stop, TitsaError


def test_create_stop(db, stop):
    db.cur.execute('SELECT * FROM stops WHERE id = :id', {'id': stop.id})
    result = db.cur.fetchone()
    assert result is not None
    assert result['id'] == stop.id
    assert result['name'] == stop.name
    assert result['cost'] == stop.cost


def test_get_stop(stop):
    stop = Stop(stop.id)
    assert stop is not None


@pytest.mark.parametrize('invalid_id', ['abc', '12345', '12a4', '1', ''])
def test_create_stop_fails_when_id_has_wrong_format(invalid_id):
    with pytest.raises(TitsaError) as exc:
        Stop(invalid_id, 'Stop Name', 1.0)
    assert str(exc.value) == f'Invalid stop ID format: {invalid_id}'


def test_create_stop_fails_when_cost_is_invalid():
    with pytest.raises(TitsaError) as exc:
        Stop('1234', 'Stop Name', -0.5)
    assert str(exc.value) == 'Invalid stop cost. Must be between 0 and 1: -0.5'

    with pytest.raises(TitsaError) as exc:
        Stop('1234', 'Stop Name', 1.5)
    assert str(exc.value) == 'Invalid stop cost. Must be between 0 and 1: 1.5'


def test_get_name(db, stop):
    db.cur.execute('SELECT * FROM stops WHERE id = :id', {'id': stop.id})
    result = db.cur.fetchone()
    assert result is not None
    assert stop.name == result['name'] == 'TAORO'


def test_get_name_when_stop_does_not_exist(db):
    stop = Stop('9999', 'Nonexistent Stop', 0.5)
    db.cur.execute(
        'DELETE FROM stops WHERE id = :id', {'id': stop.id}
    )  # Ensure the stop does not exist
    assert stop.name == ''


def test_set_name(db, stop):
    stop.name = 'NEW NAME'
    db.cur.execute('SELECT * FROM stops WHERE id = :id', {'id': stop.id})
    result = db.cur.fetchone()
    assert result is not None
    assert stop.name == result['name'] == 'NEW NAME'


def test_get_cost(db, stop):
    db.cur.execute('SELECT * FROM stops WHERE id = :id', {'id': stop.id})
    result = db.cur.fetchone()
    assert result is not None
    assert stop.cost == result['cost'] == 0.75


def test_get_cost_when_stop_does_not_exist(db):
    stop = Stop('9999', 'Nonexistent Stop', 0.5)
    db.cur.execute(
        'DELETE FROM stops WHERE id = :id', {'id': stop.id}
    )  # Ensure the stop does not exist
    assert stop.cost == 0.0


def test_set_cost(db, stop):
    stop.cost = 2.0
    db.cur.execute('SELECT * FROM stops WHERE id = :id', {'id': stop.id})
    result = db.cur.fetchone()
    assert result is not None
    assert stop.cost == result['cost'] == 2.0


def test_load_stops_from_file(db):
    stops_file = 'data/stops.csv'
    Stop.load_stops_from_file(stops_file)
    with open(stops_file) as f:
        for line in f:
            stop_id, name, cost = line.strip().split(',')
            db.cur.execute('SELECT * FROM stops WHERE id = :id', {'id': stop_id})
            result = db.cur.fetchone()
            assert result is not None
            assert result['id'] == stop_id
            assert result['name'] == name
            assert result['cost'] == float(cost)
