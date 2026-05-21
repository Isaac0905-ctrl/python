import sqlite3

from .loader import DbHandler


def test_db_handler_init():
    db = DbHandler()
    assert db is not None
    assert db.con is not None
    assert db.con.autocommit is True
    assert db.con.row_factory is sqlite3.Row
    assert db.cur is not None


def test_db_handler_run():
    db = DbHandler()
    db.run_sql('CREATE TABLE test (id INTEGER PRIMARY KEY, name TEXT)')
    db.run_sql('INSERT INTO test (name) VALUES (:name)', name='Alice')
    db.run_sql('INSERT INTO test (name) VALUES (:name)', name='Bob')
    results = db.run_sql('SELECT * FROM test')
    assert len(results) == 2
    assert results[0]['name'] == 'Alice'
    assert results[1]['name'] == 'Bob'


def test_db_handler_run_sql_with_params():
    db = DbHandler()
    db.run_sql('CREATE TABLE test (id INTEGER PRIMARY KEY, name TEXT)')
    db.run_sql('INSERT INTO test (name) VALUES (:name)', name='Charlie')
    result = db.run_sql('SELECT * FROM test WHERE name = :name', name='Charlie')
    assert len(result) == 1
    assert result[0]['name'] == 'Charlie'


def test_db_handler_run_sql_select_no_results():
    db = DbHandler()
    db.run_sql('CREATE TABLE test (id INTEGER PRIMARY KEY, name TEXT)')
    result = db.run_sql('SELECT * FROM test')
    assert len(result) == 0


def test_db_handler_run_sql_with_no_select_query():
    db = DbHandler()
    db.run_sql('CREATE TABLE test (id INTEGER PRIMARY KEY, name TEXT)')
    result = db.run_sql('INSERT INTO test (name) VALUES (:name)', name='David')
    assert result is None
