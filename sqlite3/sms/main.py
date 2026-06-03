import re
import sqlite3

DB_PATH = ':memory:'
PHONE_REGEX = r'^\+?(\d{2}\s)?[6-7]\d{8}$'


class DbHandler:
    def __init__(self, db_path: str = DB_PATH):
        self.db_path = db_path
        self.con = sqlite3.connect(db_path, check_same_thread=False)
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()

    def __del__(self):                      # ← cierra al destruirse el objeto
        try:
            self.con.close()
        except Exception:
            pass

    def create_db(self) -> None:
        self.cur.execute("""CREATE TABLE activity(
            id INTEGER PRIMARY KEY,
            sender TEXT,
            recipient TEXT,
            message TEXT
        )""")
        self.cur.execute("""CREATE TABLE access(
            phone_number TEXT PRIMARY KEY,
            pin TEXT,
            puk TEXT
        )""")
        self.con.commit()


class SMS(DbHandler):
    def __init__(self, sender: str, recipient: str, message: str):
        super().__init__()
        if not re.fullmatch(PHONE_REGEX, sender):
            raise SMSError('Sender has invalid phone format', self)
        if not re.fullmatch(PHONE_REGEX, recipient):
            raise SMSError('Recipient has invalid phone format', self)
        self.sender = sender
        self.recipient = recipient
        self.message = message

    def send(self) -> None:
        self.cur.execute(
            'INSERT INTO activity (sender, recipient, message) VALUES(?, ?, ?)',
            [self.sender, self.recipient, self.message],
        )
        self.con.commit()

    def __str__(self):
        return f'From: {self.sender}\nTo: {self.recipient}\n---\n{self.message}'


class SIM(DbHandler):
    def __init__(self, phone_number: str):
        super().__init__()
        self.phone_number = phone_number
        self.unlocked = False

    def unlock(self, pin: str, *, puk: str = '') -> None:
        result = self.cur.execute(
            'SELECT pin, puk FROM access WHERE phone_number = ?',
            [self.phone_number],
        ).fetchone()

        if result is None:
            return  # número no existe → no desbloquea, no lanza excepción

        query_pin, query_puk = result
        if pin == query_pin or puk == query_puk:
            self.unlocked = True
        else:
            raise SMSError('SIM cannot be unlocked', self)

    @staticmethod
    def unlock_required(method):
        def wrapper(self, *args, **kwargs):
            if not self.unlocked:
                raise SMSError('SMS is locked', self)
            return method(self, *args, **kwargs)
        return wrapper

    @unlock_required
    def send_sms(self, *, recipient: str, message: str) -> None:
        if not re.fullmatch(PHONE_REGEX, recipient):
            raise SMSError('Recipient has invalid phone format', self)
        self.cur.execute(
            'INSERT INTO activity (sender, recipient, message) VALUES(?, ?, ?)',
            [self.phone_number, recipient, message],
        )
        self.con.commit()

    @unlock_required
    def get_sms(self, sent: bool = True):
        field = 'sender' if sent else 'recipient'
        rows = self.cur.execute(
            f'SELECT sender, recipient, message FROM activity WHERE {field} = ?',
            [self.phone_number],
        ).fetchall()
        for row in rows:
            # Instanciamos SMS como objeto de datos, sin que abra conexión propia
            sms = object.__new__(SMS)
            sms.sender = row['sender']
            sms.recipient = row['recipient']
            sms.message = row['message']
            yield sms


class SMSError(Exception):
    def __init__(self, message: str, db_handler: DbHandler):
        super().__init__(message)
        self.message = message
        db_handler.con.close()