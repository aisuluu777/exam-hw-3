import sqlite3

class Database:
    def __init__(self, path: str):
        self.path = path

    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute('''
            CREATE TABLE IF NOT EXISTS homeworks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            number_of_hw INTEGER NOT NULL,
            link TEXT NOT NULL)''')

    def save_hw(self, data: dict):
        with sqlite3.connect(self.path) as conn:
            conn.execute('''
            INSERT INTO homeworks(name, number_of_hw, link)
            VALUES(?,?,?)''',
                         (data['name'], data['number_of_hw'], data['link']))
