import re

from .db import DbHandler
from .errors import TitsaError


class User(DbHandler):
    def __init__(self, id: str, name: str = '', credit: float = 0):
        if not re.fullmatch(r'\d{8}[A-Z]', id):
            raise TitsaError(f'Invalid user ID format: {id}')
        super().__init__()
        self.id = id
        sql = 'Insert or ignore into users (id, name, credit) values (:id, :name, :credit)'
        self.cur.execute(sql, {'id': id, 'name': name, 'credit': credit})

    @property
    def name(self) -> str:
        sql = 'Select name from users where id = :id'
        self.cur.execute(sql, {'id': self.id})
        row = self.cur.fetchone()
        return row['name'] if row else ''

    @name.setter
    def name(self, value: str) -> None:
        sql = 'Update users set name = :name where id = :id'
        self.cur.execute(sql, {'name': value, 'id': self.id})

    @property
    def credit(self) -> float:
        sql = 'Select credit from users where id = :id'
        self.cur.execute(sql, {'id': self.id})
        row = self.cur.fetchone()
        return row['credit'] if row else 0.0

    @credit.setter
    def credit(self, value: float) -> None:
        sql = 'Update users set credit = :credit where id = :id'
        self.cur.execute(sql, {'credit': value, 'id': self.id})
