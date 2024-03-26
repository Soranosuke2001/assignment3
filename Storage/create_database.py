import mysql.connector, time

from helpers.read_config import database_config

if __name__ == "__main__":
    user, password, hostname, port, db = database_config()

    time.sleep(10)

    connected = False

    while not connected:
        try:
            connection = mysql.connector.connect(host=hostname, user=user, password=password)
            connected = True
        except Exception as e:
            print("Database not yet available, retrying in 10 seconds")
            time.sleep(10)
    
    # connection = mysql.connector.connect(host=hostname, user=user, password=password)
    c = connection.cursor()

    c.execute(f"CREATE DATABASE IF NOT EXISTS {db}")

    connection.commit()
    connection.close()

    connection = mysql.connector.connect(host=hostname, user=user, password=password, database=db)

    c = connection.cursor()

    create_table1 = '''
                    CREATE TABLE IF NOT EXISTS gun_stats
                    (
                        id INT NOT NULL AUTO_INCREMENT,
                        trace_id VARCHAR(250) NOT NULL,
                        game_id VARCHAR(250) NOT NULL,
                        gun_id VARCHAR(250) NOT NULL,
                        user_id VARCHAR(250) NOT NULL,
                        num_bullets_shot INTEGER NOT NULL,
                        num_body_shots INTEGER NOT NULL,
                        num_head_shots INTEGER NOT NULL,
                        num_missed_shots INTEGER NOT NULL,
                        date_created DATETIME NOT NULL,
                        CONSTRAINT gun_stat_pk PRIMARY KEY (id)
                    )
                    '''

    create_table2 = '''
                    CREATE TABLE IF NOT EXISTS purchase_history
                    (
                        id INT NOT NULL AUTO_INCREMENT,
                        trace_id VARCHAR(250) NOT NULL,
                        transaction_id VARCHAR(250) NOT NULL,
                        item_id VARCHAR(250) NOT NULL,
                        user_id VARCHAR(250) NOT NULL,
                        item_price INTEGER NOT NULL,
                        transaction_date VARCHAR(100) NOT NULL,
                        date_created DATETIME NOT NULL,
                        CONSTRAINT purchase_history_pk PRIMARY KEY (id)
                    )
                    '''

    c.execute(create_table1)
    c.execute(create_table2)

    connection.commit()
    connection.close()
