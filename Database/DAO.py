from sqlite3 import Connection

class DAO(object):
    __conn: Connection
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn
    def insert_book(book)