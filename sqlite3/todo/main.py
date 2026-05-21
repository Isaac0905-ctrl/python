from __future__ import annotations

import sqlite3

DB_PATH = ':memory:'

TASK_DONE_SYMBOL = '[X]'
TASK_PENDING_SYMBOL = '[ ]'


def create_db(db_path: str = DB_PATH) -> None:
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    sql = """CREATE TABLE tasks (
        id INTEGER PRIMARY KEY,
        name TEXT,
        done INTEGER
    )"""
    cur.execute(sql)
    con.commit()
    ...


class Task:
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    con.row_factory = sqlite3.Row

    def __init__(self, name: str, done: bool = False, id: int = -1):
        self.name = name
        self.done = done
        self.id = id

    def save(self) -> None:
        query_one = 'INSERT INTO tasks (name, done) VALUES (?, ?)'
        self.cur.execute(query_one, [self.name, int(self.done)])
        self.con.commit()

        query = 'SELECT id FROM tasks WHERE name = ? AND done = ? ORDER BY id DESC LIMIT 1'
        self.cur.execute(query, [self.name, self.done])
        self.id = self.cur.fetchone()[0]

    def update(self) -> None:
        query = 'UPDATE tasks SET name = ?, done = ? WHERE id = ?'
        self.cur.execute(query, [self.name, self.done, self.id])
        self.con.commit()

    def check(self) -> None:
        self.done = True
        self.update()

    def uncheck(self) -> None:
        self.done = False
        self.update()

    def __repr__(self):
        mark = TASK_DONE_SYMBOL if self.done else TASK_PENDING_SYMBOL
        return f'{mark} {self.name} (id={self.id})'

    @classmethod
    def from_db_row(cls, row: sqlite3.Row) -> Task:
        return cls(name=row['name'], done=row['done'], id=row['id'])

    @classmethod
    def get(cls, task_id: int) -> Task | None:
        cls.cur.execute('SELECT * FROM tasks where id = ?', (task_id,))
        row = cls.cur.fetchone()
        if row is None:
            return None
        return cls.from_db_row(row)


class ToDo:
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    def get_tasks(self, done: int = -1):
        if done == -1:
            self.cur.execute('SELECT * FROM tasks')
        else:
            self.cur.execute('SELECT * from tasks WHERE done = ?', (done,))
        for row in self.cur.fetchall():
            yield Task.from_db_row(row)