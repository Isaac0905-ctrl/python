import re

from .db import DbHandler
from .errors import TitsaError
from .stops import Stop
from .users import User


class Bus(DbHandler):
    def __init__(self, id: str, total_seats: int = 0):
        if not re.fullmatch(r'\d{2,3}', id):
            raise TitsaError(f'Invalid bus ID format: {id}')
        super().__init__()
        self.id = id
        sql = 'Insert or ignore into buses (id, total_seats, busy_seats) values (:id, :total_seats, 0)'
        self.cur.execute(sql, {'id': id, 'total_seats': total_seats})

    @property
    def total_seats(self) -> int:
        sql = 'Select total_seats from buses where id = :id'
        self.cur.execute(sql, {'id': self.id})
        row = self.cur.fetchone()
        return row['total_seats'] if row else 0

    @total_seats.setter
    def total_seats(self, value: int):
        sql = 'Update buses set total_seats = :value where id = :id'
        self.cur.execute(sql, {'value': value, 'id': self.id})

    @property
    def busy_seats(self) -> int:
        sql = 'Select busy_seats from buses where id = :id'
        self.cur.execute(sql, {'id': self.id})
        row = self.cur.fetchone()
        return row['busy_seats'] if row else 0

    @busy_seats.setter
    def busy_seats(self, value: int):
        sql = 'Update buses set busy_seats = :value where id = :id'
        self.cur.execute(sql, {'value': value, 'id': self.id})

    def add_stop(self, stop: Stop, stop_order: int) -> None:
        sql = 'Insert into route (bus_id, stop_id, stop_order) values (:bus_id, :stop_id, :stop_order)'
        self.cur.execute(sql, {'bus_id': self.id, 'stop_id': stop.id, 'stop_order': stop_order})

    def load_route_from_file(self, filename: str) -> None:
        with open(filename) as f:
            for line in f:
                line = line.strip()
                parts = line.split(',')
                bus_id, stop_order, stop_id = parts[0], int(parts[1]), parts[2]
                if bus_id == self.id:
                    stop = Stop(stop_id)
                    self.add_stop(stop, stop_order)

    @property
    def is_full(self) -> bool:
        return self.busy_seats >= self.total_seats

    @property
    def first_stop(self) -> Stop | None:
        sql = 'Select stop_id from route where bus_id = :id order by stop_order asc limit 1'
        self.cur.execute(sql, {'id': self.id})
        row = self.cur.fetchone()
        return Stop(row['stop_id']) if row else None

    @property
    def last_stop(self) -> Stop | None:
        sql = 'Select stop_id from route where bus_id = :id order by stop_order desc limit 1'
        self.cur.execute(sql, {'id': self.id})
        row = self.cur.fetchone()
        return Stop(row['stop_id']) if row else None

    def get_stops(self, from_stop: Stop | None = None, to_stop: Stop | None = None):
        if from_stop is None:
            from_stop = self.first_stop
        if to_stop is None:
            to_stop = self.last_stop
        if from_stop is None or to_stop is None:
            return

        sql = 'Select stop_id, stop_order from route where bus_id = :bus_id and (stop_id = :from_id or stop_id = :to_id)'
        self.cur.execute(sql, {'bus_id': self.id, 'from_id': from_stop.id, 'to_id': to_stop.id})
        rows = {row['stop_id']: row['stop_order'] for row in self.cur.fetchall()}

        if from_stop.id not in rows or to_stop.id not in rows:
            return

        from_order = rows[from_stop.id]
        to_order = rows[to_stop.id]

        query = """Select stop_id from route where
        bus_id = :bus_id and stop_order >= :from_order
        and stop_order <= :to_order order by stop_order asc"""
        self.cur.execute(query, {'bus_id': self.id, 'from_order': from_order, 'to_order': to_order})
        for row in self.cur.fetchall():
            yield Stop(row['stop_id'])

    # ==============================================================================
    # User management
    # ==============================================================================

    def user_is_on_bus(self, user: User) -> bool:
        sql = """Select status from trip where user_id = :user_id
        and bus_id = :bus_id order by moment desc limit 1"""
        self.cur.execute(sql, {'user_id': user.id, 'bus_id': self.id})
        row = self.cur.fetchone()
        return row is not None and row['status'] == 'IN'

    def user_last_trip_cost(self, user: User) -> float:
        sql = """Select stop_id, status from trip where user_id = :user_id
        and bus_id = :bus_id order by moment desc limit 2"""
        self.cur.execute(sql, {'user_id': user.id, 'bus_id': self.id})
        rows = self.cur.fetchall()
        if len(rows) < 2:
            return 0.0
        out_row, in_row = rows[0], rows[1]
        if out_row['status'] != 'OUT' or in_row['status'] != 'IN':
            return 0.0
        from_stop = Stop(in_row['stop_id'])
        to_stop = Stop(out_row['stop_id'])
        return sum(stop.cost for stop in self.get_stops(from_stop, to_stop))

    def user_trip(self, user: User, stop: Stop, status: str) -> None:
        sql = """Insert into trip (user_id, bus_id, stop_id, moment, status)
        values (:user_id, :bus_id, :stop_id, datetime('now', 'subsec'), :status)"""
        self.cur.execute(
            sql, {'user_id': user.id, 'bus_id': self.id, 'stop_id': stop.id, 'status': status}
        )

    def user_get_on(self, user: User, stop: Stop) -> None:
        if self.user_is_on_bus(user):
            raise TitsaError(f'User {user.id} is already on bus {self.id}')
        if self.is_full:
            raise TitsaError(f'Bus {self.id} is full')
        self.user_trip(user, stop, 'IN')
        self.busy_seats = self.busy_seats + 1

    def user_get_off(self, user: User, stop: Stop) -> None:
        if not self.user_is_on_bus(user):
            raise TitsaError(f'User {user.id} is not on bus {self.id}')
        self.user_trip(user, stop, 'OUT')
        self.busy_seats = self.busy_seats - 1
        user.credit = user.credit - self.user_last_trip_cost(user)
