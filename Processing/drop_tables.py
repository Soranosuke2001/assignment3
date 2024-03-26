import sqlite3

from helpers.read_config import get_sqlite_config

filename, seconds, url = get_sqlite_config()

connection = sqlite3.connect(filename)

c = connection.cursor()

drop_table1 = 'DROP TABLE IF EXISTS stats'

c.execute(drop_table1)

connection.commit()
connection.close()

