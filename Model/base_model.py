import sqlite3
from abc import abstractmethod, ABC
class BaseModel(ABC):

    db_name = './data/demo.db'

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def create(cls: type, **kwargs)-> tuple:
        with sqlite3.connect(cls.db_name) as conn:
            cursor = conn.cursor()
            columns = ', '.join(kwargs.keys())
            placeholders = ', '.join('?' for _ in kwargs)
            cursor.execute(f"INSERT INTO {cls.__name__} ({columns}) VALUES ({placeholders}) RETURNING *", list(kwargs.values()))
            return cursor.fetchone()
    
    def read(cls, **kwargs):
        OPERATORS = {
            'gt': '>',
            'lt': '<',
            'gte': '>=',
            'lte': '<=',
            'eq': '=',
            'ne': '!='
        }
        with sqlite3.connect(cls.db_name) as conn:
            cursor = conn.cursor()
            conditions = []
            values = []
            for key, value in kwargs.items():
                field, op = key.split('__')
                sql_op = OPERATORS.get(op, '=')
                conditions.append(f"{field} {sql_op} ?")
                values.append(value)
            conditions_str = ' AND '.join(conditions)
            request_str = f"SELECT * FROM {cls.__name__}"
            if conditions_str:
                request_str += f" WHERE {conditions_str}"
            cursor.execute(request_str, values)
            return cursor.fetchall()

    def update(self, **kwargs):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            updates = ', '.join(f"{key} = ?" for key in kwargs)
            cursor.execute(f"UPDATE {self.__class__.__name__} SET {updates} WHERE id = ?", list(kwargs.values()) + [self.id])

    def delete(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM {self.__class__.__name__} WHERE id = ?", [self.id])