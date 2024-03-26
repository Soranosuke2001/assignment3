import sqlite3

from helpers.read_config import get_sqlite_config

filename, seconds, url = get_sqlite_config()

connection = sqlite3.connect(filename)

c = connection.cursor()

create_table1 = '''
                CREATE TABLE IF NOT EXISTS stats
                (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    num_gun_stat_events INTEGER NOT NULL,
                    head_shot_count INTEGER NOT NULL,
                    bullet_shot_count INTEGER NOT NULL,
                    num_purchase_history_events INTEGER NOT NULL,
                    total_revenue INTEGER NOT NULL,
                    last_updated DATETIME NOT NULL
                )
                '''

c.execute(create_table1)

connection.commit()
connection.close()

