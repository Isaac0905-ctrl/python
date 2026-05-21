import sqlite3
from pathlib import Path

import pytest

from .loader import Bus, Stop, User, settings


class Database:
    def __init__(self, db_path: str = ':memory:'):
        self.path = db_path
        self.con = sqlite3.connect(db_path, autocommit=True)
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()


@pytest.fixture
def empty_db():
    db_path = settings.DB_PATH
    db = Database(db_path)
    yield db
    db.con.close()


@pytest.fixture(autouse=True)
def db(empty_db):
    # Table users
    sql = """CREATE TABLE IF NOT EXISTS users (
id TEXT PRIMARY KEY,
name TEXT NOT NULL,
credit REAL DEFAULT 0
);"""
    empty_db.cur.execute(sql)

    # Table buses
    sql = """CREATE TABLE IF NOT EXISTS buses (
id TEXT PRIMARY KEY,
total_seats INTEGER NOT NULL,
busy_seats INTEGER NOT NULL DEFAULT 0,
CHECK (total_seats >= 0),
CHECK (busy_seats >= 0),
CHECK (busy_seats <= total_seats)
);"""
    empty_db.cur.execute(sql)

    # Table stops
    sql = """CREATE TABLE IF NOT EXISTS stops (
id TEXT PRIMARY KEY,
name TEXT NOT NULL,
cost REAL DEFAULT 0
);"""
    empty_db.cur.execute(sql)

    # Table trip
    sql = """CREATE TABLE IF NOT EXISTS trip (
user_id TEXT NOT NULL,
bus_id TEXT NOT NULL,
stop_id TEXT NOT NULL,
moment DATETIME NOT NULL,
status TEXT NOT NULL,
PRIMARY KEY (user_id, bus_id, moment)
FOREIGN KEY (user_id) REFERENCES users(id),
FOREIGN KEY (bus_id) REFERENCES buses(id),
FOREIGN KEY (stop_id) REFERENCES stops(id)
);"""
    empty_db.cur.execute(sql)

    # Table route
    sql = """CREATE TABLE IF NOT EXISTS route (
bus_id TEXT NOT NULL,
stop_id TEXT NOT NULL,
stop_order INTEGER NOT NULL,
PRIMARY KEY (bus_id, stop_id)
FOREIGN KEY (bus_id) REFERENCES buses(id),
FOREIGN KEY (stop_id) REFERENCES stops(id)
);"""
    empty_db.cur.execute(sql)
    yield empty_db
    empty_db.con.close()


@pytest.fixture(autouse=True)
def destroy_db():
    db_path = settings.DB_PATH
    yield
    Path(db_path).unlink(missing_ok=True)


@pytest.fixture
def user():
    return User('76548951T', 'Guido van Rossum', 100)


@pytest.fixture
def bus():
    return Bus('102', 50)


@pytest.fixture
def stop():
    return Stop('4095', 'TAORO', 0.75)
