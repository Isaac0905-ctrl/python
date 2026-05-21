import inspect
import time

import pytest

from .loader import Bus, Stop, TitsaError


def test_create_bus(db, bus):
    db.cur.execute('SELECT * FROM buses WHERE id = :id', {'id': bus.id})
    result = db.cur.fetchone()
    assert result is not None
    assert result['id'] == bus.id
    assert result['total_seats'] == bus.total_seats
    assert result['busy_seats'] == bus.busy_seats


def test_get_bus(bus):
    bus = Bus(bus.id)
    assert bus is not None


@pytest.mark.parametrize('invalid_id', ['abc', '12345', '12a4', '4532', '1', ''])
def test_create_bus_fails_when_id_has_wrong_format(invalid_id):
    with pytest.raises(TitsaError) as exc:
        Bus(invalid_id, 50)
    assert str(exc.value) == f'Invalid bus ID format: {invalid_id}'


def test_get_total_seats(db, bus):
    db.cur.execute('SELECT * FROM buses WHERE id = :id', {'id': bus.id})
    result = db.cur.fetchone()
    assert result is not None
    assert bus.total_seats == result['total_seats'] == 50


def test_get_total_seats_when_bus_does_not_exist(db):
    bus = Bus('999', 0)
    db.cur.execute(
        'DELETE FROM buses WHERE id = :id', {'id': bus.id}
    )  # Ensure the bus does not exist
    assert bus.total_seats == 0


def test_set_total_seats(db, bus):
    bus.total_seats = 60
    db.cur.execute('SELECT * FROM buses WHERE id = :id', {'id': bus.id})
    result = db.cur.fetchone()
    assert result is not None
    assert bus.total_seats == result['total_seats'] == 60


def test_get_busy_seats(db, bus):
    db.cur.execute('SELECT * FROM buses WHERE id = :id', {'id': bus.id})
    result = db.cur.fetchone()
    assert result is not None
    assert bus.busy_seats == result['busy_seats'] == 0


def test_get_busy_seats_when_bus_does_not_exist(db):
    bus = Bus('999', 0)
    db.cur.execute(
        'DELETE FROM buses WHERE id = :id', {'id': bus.id}
    )  # Ensure the bus does not exist
    assert bus.busy_seats == 0


def test_set_busy_seats(db, bus):
    bus.busy_seats = 10
    db.cur.execute('SELECT * FROM buses WHERE id = :id', {'id': bus.id})
    result = db.cur.fetchone()
    assert result is not None
    assert bus.busy_seats == result['busy_seats'] == 10


def test_add_stop(db, bus, stop):
    bus.add_stop(stop, stop_order=1)
    db.cur.execute(
        'SELECT * FROM route WHERE bus_id = :bus_id AND stop_id = :stop_id',
        {'bus_id': bus.id, 'stop_id': stop.id},
    )
    result = db.cur.fetchone()
    assert result is not None
    assert result['bus_id'] == bus.id
    assert result['stop_id'] == stop.id
    assert result['stop_order'] == 1


def test_load_route_from_file(db, bus):
    route_file = 'data/routes.csv'
    bus.load_route_from_file(route_file)
    with open(route_file) as f:
        for line in f:
            bus_id, stop_order, stop_id = line.strip().split(',')
            if bus_id == bus.id:
                db.cur.execute(
                    'SELECT * FROM route WHERE bus_id = :bus_id AND stop_id = :stop_id',
                    {'bus_id': bus.id, 'stop_id': stop_id},
                )
                result = db.cur.fetchone()
                assert result is not None
                assert result['bus_id'] == bus.id
                assert result['stop_id'] == stop_id
                assert result['stop_order'] == int(stop_order)


def test_bus_is_full(bus):
    bus.total_seats = 2
    bus.busy_seats = 2
    assert bus.is_full


def test_get_bus_first_stop(bus):
    stop1 = Stop('0001', 'Stop 1', 1.0)
    stop2 = Stop('0002', 'Stop 2', 1.0)
    stop3 = Stop('0003', 'Stop 3', 1.0)
    bus.add_stop(stop1, stop_order=1)
    bus.add_stop(stop2, stop_order=2)
    bus.add_stop(stop3, stop_order=3)

    first_stop = bus.first_stop
    assert first_stop is not None
    assert first_stop.id == stop1.id
    assert first_stop.name == stop1.name
    assert first_stop.cost == stop1.cost


def test_get_bus_first_stop_no_stops(bus):
    first_stop = bus.first_stop
    assert first_stop is None


def test_get_bus_last_stop(bus):
    stop1 = Stop('0001', 'Stop 1', 1.0)
    stop2 = Stop('0002', 'Stop 2', 1.0)
    stop3 = Stop('0003', 'Stop 3', 1.0)
    bus.add_stop(stop1, stop_order=1)
    bus.add_stop(stop2, stop_order=2)
    bus.add_stop(stop3, stop_order=3)

    last_stop = bus.last_stop
    assert last_stop is not None
    assert last_stop.id == stop3.id
    assert last_stop.name == stop3.name
    assert last_stop.cost == stop3.cost


def test_get_bus_last_stop_no_stops(bus):
    last_stop = bus.last_stop
    assert last_stop is None


def test_get_stops_is_a_generator(bus):
    assert inspect.isgeneratorfunction(bus.get_stops)


def test_get_stops_works_as_expected(bus):
    stop1 = Stop('0001', 'Stop 1', 1.0)
    stop2 = Stop('0002', 'Stop 2', 1.0)
    stop3 = Stop('0003', 'Stop 3', 1.0)
    bus.add_stop(stop1, stop_order=1)
    bus.add_stop(stop2, stop_order=2)
    bus.add_stop(stop3, stop_order=3)

    stops = list(bus.get_stops(from_stop=stop1, to_stop=stop3))
    assert len(stops) == 3
    assert stops[0].id == stop1.id
    assert stops[1].id == stop2.id
    assert stops[2].id == stop3.id


# ==============================================================================
# User management
# ==============================================================================


def test_user_is_on_bus(bus, user, stop):
    bus.add_stop(stop, stop_order=1)
    bus.user_get_on(user, stop)
    assert bus.user_is_on_bus(user)


def test_user_is_not_on_bus(bus, user):
    assert not bus.user_is_on_bus(user)


def test_user_last_trip_cost(bus, user):
    stop1 = Stop('0001', 'Stop 1', 0.1)
    stop2 = Stop('0002', 'Stop 2', 0.2)
    stop3 = Stop('0003', 'Stop 3', 0.3)
    stop4 = Stop('0004', 'Stop 4', 0.4)
    stop5 = Stop('0005', 'Stop 5', 0.5)

    bus.add_stop(stop1, stop_order=1)
    bus.add_stop(stop2, stop_order=2)
    bus.add_stop(stop3, stop_order=3)
    bus.add_stop(stop4, stop_order=4)
    bus.add_stop(stop5, stop_order=5)

    bus.user_get_on(user, stop2)
    time.sleep(1)  # Ensure the trip records have different timestamps
    bus.user_get_off(user, stop4)

    cost = bus.user_last_trip_cost(user)
    assert cost == 0.9


# ==============================================================================
# User get on bus
# ==============================================================================


def test_user_get_on(db, bus, user, stop):
    bus.total_seats = 2
    bus.busy_seats = 0
    bus.user_get_on(user, stop)
    db.cur.execute('SELECT * FROM trip WHERE user_id = :user_id', {'user_id': user.id})
    result = db.cur.fetchone()
    assert result is not None
    assert result['user_id'] == user.id
    assert result['bus_id'] == bus.id
    assert result['stop_id'] == stop.id


def test_user_get_on_updates_busy_seats(bus, user, stop):
    bus.total_seats = 2
    bus.busy_seats = 0
    bus.user_get_on(user, stop)
    assert bus.busy_seats == 1


def test_user_get_on_fails_when_user_is_already_on_bus(bus, user, stop):
    bus.total_seats = 2
    bus.busy_seats = 0
    bus.user_get_on(user, stop)
    with pytest.raises(TitsaError) as exc:
        bus.user_get_on(user, stop)
    assert str(exc.value) == f'User {user.id} is already on bus {bus.id}'


def test_user_get_on_fails_when_bus_is_full(bus, user, stop):
    bus.total_seats = 2
    bus.busy_seats = 2
    with pytest.raises(TitsaError) as exc:
        bus.user_get_on(user, stop)
    assert str(exc.value) == f'Bus {bus.id} is full'


# ==============================================================================
# User get off bus
# ==============================================================================


def test_user_get_off(db, bus, user):
    stop1 = Stop('0001', 'Stop 1', 1.0)
    stop2 = Stop('0002', 'Stop 2', 1.0)
    stop3 = Stop('0003', 'Stop 3', 1.0)
    stop4 = Stop('0004', 'Stop 4', 1.0)
    stop5 = Stop('0005', 'Stop 5', 1.0)

    bus.add_stop(stop1, stop_order=1)
    bus.add_stop(stop2, stop_order=2)
    bus.add_stop(stop3, stop_order=3)
    bus.add_stop(stop4, stop_order=4)
    bus.add_stop(stop5, stop_order=5)

    initial_credit = user.credit
    bus.user_get_on(user, stop1)
    time.sleep(1)  # Ensure the trip records have different timestamps
    bus.user_get_off(user, stop5)

    # Check that user did get off the bus and that the trip was recorded correctly
    db.cur.execute(
        'SELECT * FROM trip WHERE user_id = :user_id ORDER BY moment DESC LIMIT 1',
        {'user_id': user.id},
    )
    result = db.cur.fetchone()
    assert result is not None
    assert result['user_id'] == user.id
    assert result['bus_id'] == bus.id
    assert result['stop_id'] == stop5.id
    assert result['status'] == 'OUT'

    # Check that the bus's busy seats were updated correctly
    assert bus.busy_seats == 0

    # Check that the user's credit was deducted correctly
    db.cur.execute('SELECT * FROM users WHERE id = :id', {'id': user.id})
    result = db.cur.fetchone()
    assert result is not None
    assert user.credit == result['credit'] == initial_credit - 5


def test_user_get_off_fails_when_user_is_not_on_bus(bus, user, stop):
    bus.total_seats = 2
    bus.busy_seats = 0
    with pytest.raises(TitsaError) as exc:
        bus.user_get_off(user, stop)
    assert str(exc.value) == f'User {user.id} is not on bus {bus.id}'
