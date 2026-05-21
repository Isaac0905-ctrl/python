import os

if os.path.exists('solution'):
    from solution import helpers
else:
    from src import helpers  # type: ignore

# ==============================================================================
# Table users
# ==============================================================================


def test_create_db_table_users(empty_db):
    helpers.create_db(empty_db.path)
    empty_db.cur.execute("PRAGMA table_info('users')")
    table = empty_db.cur.fetchall()
    assert len(table) == 3
    assert table[0]['name'] == 'id'
    assert table[0]['type'] == 'TEXT'
    assert table[0]['pk'] == 1
    assert table[1]['name'] == 'name'
    assert table[1]['type'] == 'TEXT'
    assert table[1]['notnull'] == 1
    assert table[2]['name'] == 'credit'
    assert table[2]['type'] == 'REAL'
    assert table[2]['dflt_value'] == '0'


def test_create_db_table_users_if_exists(empty_db):
    helpers.create_db(empty_db.path)
    helpers.create_db(empty_db.path)  # should not raise an error
    empty_db.cur.execute("PRAGMA table_info('users')")
    table = empty_db.cur.fetchall()
    assert len(table) == 3


# ==============================================================================
# Table buses
# ==============================================================================


def test_create_db_table_buses(empty_db):
    helpers.create_db(empty_db.path)
    empty_db.cur.execute("PRAGMA table_info('buses')")
    table = empty_db.cur.fetchall()
    assert len(table) == 3
    assert table[0]['name'] == 'id'
    assert table[0]['type'] == 'TEXT'
    assert table[0]['pk'] == 1
    assert table[1]['name'] == 'total_seats'
    assert table[1]['type'] == 'INTEGER'
    assert table[1]['notnull'] == 1
    assert table[2]['name'] == 'busy_seats'
    assert table[2]['type'] == 'INTEGER'
    assert table[2]['dflt_value'] == '0'


def test_create_db_table_buses_if_exists(empty_db):
    helpers.create_db(empty_db.path)
    helpers.create_db(empty_db.path)  # should not raise an error
    empty_db.cur.execute("PRAGMA table_info('buses')")
    table = empty_db.cur.fetchall()
    assert len(table) == 3


# ==============================================================================
# Table stops
# ==============================================================================


def test_create_db_table_stops(empty_db):
    helpers.create_db(empty_db.path)
    empty_db.cur.execute("PRAGMA table_info('stops')")
    table = empty_db.cur.fetchall()
    assert len(table) == 3
    assert table[0]['name'] == 'id'
    assert table[0]['type'] == 'TEXT'
    assert table[0]['pk'] == 1
    assert table[1]['name'] == 'name'
    assert table[1]['type'] == 'TEXT'
    assert table[1]['notnull'] == 1
    assert table[2]['name'] == 'cost'
    assert table[2]['type'] == 'REAL'


def test_create_db_table_stops_if_exists(empty_db):
    helpers.create_db(empty_db.path)
    helpers.create_db(empty_db.path)  # should not raise an error
    empty_db.cur.execute("PRAGMA table_info('stops')")
    table = empty_db.cur.fetchall()
    assert len(table) == 3


# ==============================================================================
# Table trip
# ==============================================================================


def test_create_db_table_trip(empty_db):
    helpers.create_db(empty_db.path)
    empty_db.cur.execute("PRAGMA table_info('trip')")
    table = empty_db.cur.fetchall()
    assert len(table) == 5
    assert table[0]['name'] == 'user_id'
    assert table[0]['type'] == 'TEXT'
    assert table[0]['pk'] == 1
    assert table[1]['name'] == 'bus_id'
    assert table[1]['type'] == 'TEXT'
    assert table[1]['pk'] == 2
    assert table[2]['name'] == 'stop_id'
    assert table[2]['type'] == 'TEXT'
    assert table[2]['pk'] == 0
    assert table[3]['name'] == 'moment'
    assert table[3]['type'] == 'DATETIME'
    assert table[3]['pk'] == 3
    assert table[4]['name'] == 'status'
    assert table[4]['type'] == 'TEXT'
    assert table[4]['pk'] == 0
    assert table[4]['notnull'] == 1


def test_create_db_table_trip_if_exists(empty_db):
    helpers.create_db(empty_db.path)
    helpers.create_db(empty_db.path)  # should not raise an error
    empty_db.cur.execute("PRAGMA table_info('trip')")
    table = empty_db.cur.fetchall()
    assert len(table) == 5


# ==============================================================================
# Table route
# ==============================================================================


def test_create_db_table_route(empty_db):
    helpers.create_db(empty_db.path)
    empty_db.cur.execute("PRAGMA table_info('route')")
    table = empty_db.cur.fetchall()
    assert len(table) == 3
    assert table[0]['name'] == 'bus_id'
    assert table[0]['type'] == 'TEXT'
    assert table[0]['pk'] == 1
    assert table[1]['name'] == 'stop_id'
    assert table[1]['type'] == 'TEXT'
    assert table[1]['pk'] == 2
    assert table[2]['name'] == 'stop_order'
    assert table[2]['type'] == 'INTEGER'
    assert table[2]['pk'] == 0
    assert table[2]['notnull'] == 1


def test_create_db_table_route_if_exists(empty_db):
    helpers.create_db(empty_db.path)
    helpers.create_db(empty_db.path)  # should not raise an error
    empty_db.cur.execute("PRAGMA table_info('route')")
    table = empty_db.cur.fetchall()
    assert len(table) == 3
