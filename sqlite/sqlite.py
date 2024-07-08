import sqlite3

# create a class to handle the database
# it should be abstract to allow a user to do a query, insert, or transaction with a separate params variable
# it should be type annotated

class Database:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def query(self, query: str, params: tuple):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def insert(self, query: str, params: tuple):
        self.cursor.execute(query, params)
        self.conn.commit()

    def transaction(self, queries: list):
        for query in queries:
            self.cursor.execute(query)
        self.conn.commit()

    def __del__(self):
        self.conn.close()
