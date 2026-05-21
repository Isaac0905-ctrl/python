import sqlite3

from .settings import DB_PATH


class DbHandler:
    def __init__(self, db_path: str = DB_PATH):
        self.con = sqlite3.connect(db_path, autocommit=True)
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()

    def run_sql(self, query: str, **params):
        self.cur.execute(query, params)
        if query.strip().upper().startswith('SELECT'):
            return self.cur.fetchall()

    def __del__(self):
        if hasattr(self, 'con') and self.con is not None:
            self.con.close()
