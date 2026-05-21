import re

from .db import DbHandler
from .errors import TitsaError


class Stop(DbHandler):
    def __init__(self, id: str, name: str = '', cost: float = 0):
        if not re.fullmatch(r'\d{4}', id):
            raise TitsaError(f'Invalid stop ID format: {id}')
        if not (0 <= cost <= 1):
            raise TitsaError(f'Invalid stop cost. Must be between 0 and 1: {cost}')
        super().__init__()
        self.id = id
        sql = 'Insert or ignore into stops (id, name, cost) values (:id, :name, :cost)'
        self.cur.execute(sql, {'id': id, 'name': name, 'cost': cost})

    @property
    def name(self) -> str:
        sql = 'Select name from stops where id = :id'
        self.cur.execute(sql, {'id': self.id})
        row = self.cur.fetchone()
        return row['name'] if row else ''

    @name.setter
    def name(self, value: str) -> None:
        sql = 'Update stops set name = :name where id = :id'
        self.cur.execute(sql, {'name': value, 'id': self.id})

    @property
    def cost(self) -> float:
        sql = 'Select cost from stops where id = :id'
        self.cur.execute(sql, {'id': self.id})
        row = self.cur.fetchone()
        return row['cost'] if row else 0.0

    @cost.setter
    def cost(self, value: float) -> None:
        sql = 'Update stops set cost = :cost where id = :id'
        self.cur.execute(sql, {'cost': value, 'id': self.id})

    @classmethod
    def load_stops_from_file(cls, filename: str) -> None:
        with open(filename) as f:
            for line in f:
                line = line.strip()
                parts = line.split(',')
                stop_id, name, cost = parts[0], parts[1], float(parts[2])
                cls(stop_id, name, cost)
