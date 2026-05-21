import sqlite3

DB_PATH = ':memory:'


class DbHandler:
    def __init__(self, db_path: str = DB_PATH):
        self.db_path = db_path
        self.con = sqlite3.connect(db_path)
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()

    def create_db(self) -> None:
        create_table_activity = """CREATE TABLE activity(
            id INTEGER PRIMARY KEY,
            sender TEXT,
            recipient TEXT,
            message TEXT
        )"""
        self.cur.execute(create_table_activity)

        create_table_access = """CREATE TABLE access(
            phone_number TEXT PRIMARY KEY,
            pin TEXT,
            puk TEXT
        )"""
        self.cur.execute(create_table_access)
        self.con.commit()


class SMS(DbHandler):
    def __init__(self, sender: str, recipient: str, message: str):
        super().__init__()
        regex = r'\+?(\d{2})?\s[6-7](\d{8})'
        self.sender = sender
        self.recipient = recipient
        self.message = message
        if sender != regex:
            message_exception = 'Sender has invalid phone format'
            raise SMSError(message_exception)
        self.recipient = recipient
        if recipient != regex:
            message_exception = 'Sender has invalid phone format'
            raise SMSError(message_exception)

    def send(self) -> None:
        query_insert = """INSERT INTO activiy (sender, recipient, message) VALUES(?, ?, ?)"""
        self.cur.execute(query_insert, [self.sender, self.recipient, self.message])

    def __str__(self):
        return f'From: {self.sender}\nTo: {self.recipient}\n---\n{self.message}'


class SIM(DbHandler):
    def __init__(self, phone_number: str):
        super().__init__()
        self.phone_number = phone_number
        self.unlocked = False

    def unlock(self, pin: str, *, puk: str = '') -> None:
        query = 'SELECT pin, puk FROM access WHERE = ?'
        query = self.cur.execute(query, [self.phone_number])
        query_pin, query_punk = query.fetchone()

        if pin == query_pin:
            self.unlock = True
        else:
            if puk == query_punk:
                self.unlock = True
            else:
                raise SMSError('SIM cannot be unlocked')

    @staticmethod
    def unlock_required(method): ...

    @unlock_required
    def send_sms(self, *, recipient: str, message: str) -> None: ...

    @unlock_required
    def get_sms(self, sent: bool = True): ...


class SMSError(Exception):
    def __init__(self, message: str, db_handler: DbHandler):
        super().__init__()
        self.message = message
