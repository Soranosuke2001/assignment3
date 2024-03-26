import mysql.connector
from helpers.read_config import database_config

user, password, hostname, port, db = database_config()

connection = mysql.connector.connect(host=hostname, user=user, password=password, database=db)

c = connection.cursor()

drop_tables = "DROP TABLE IF EXISTS gun_stats, purchase_history"

c.execute(drop_tables)

connection.commit()
connection.close()