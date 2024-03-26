import csv
import uuid
import random
from datetime import datetime, timedelta


with open("transactions.csv", "w", newline="") as file:
    writer = csv.DictWriter(
        file, fieldnames=["transaction_id", "user_id", "item_id"])
    writer.writeheader()

    for _ in range(1500):
        writer.writerow({
            "transaction_id": uuid.uuid4(),
            "user_id": uuid.uuid4(),
            "item_id": uuid.uuid4(),
        })


with open("users.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["game_id", "user_id", "gun_id"])
    writer.writeheader()

    for _ in range(1500):
        writer.writerow({
            "game_id": uuid.uuid4(),
            "user_id": uuid.uuid4(),
            "gun_id": uuid.uuid4(),
        })


datetimes = []
start_date = datetime(2020, 1, 1)
end_date = datetime(2024, 12, 31)

for _ in range(1000):
    random_date = start_date + \
        timedelta(days=random.randint(0, (end_date - start_date).days))
    random_time = timedelta(hours=random.randint(
        0, 23), minutes=random.randint(0, 59), seconds=random.randint(0, 59))
    random_datetime = random_date + random_time

    datetimes.append(random_datetime)


with open("dates.csv", mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["id", "date"])
    writer.writeheader()

    for date in datetimes:
        writer.writerow({
            "id": uuid.uuid4(),
            "date": date.strftime("%Y-%m-%dT%H:%M:%SZ")
        })
