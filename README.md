# ACIT 3855 Microservices Project

### Description

This project is to demonstrate the microservices architecture. This application will receive 2 different types of events (Receiver Service) and will store the events to the database (Storage Service). There is a periodic processing service (Processing Service) that will calculate some statistics based on the data received. The Audit Service will allow users to fetch a specific event that was received previously. There is also a website (Dashboard Service) that will allow the user to view the statistics and is regularly updated.

### Getting Started

1. On your machine, make sure you have Docker and Git installed
2. Clone this repository to your machine
   Note: You may have to change the configuration files.
   - In every folder, but `Dashboard` folder, there is a `config` folder. You may have to edit the `app_conf.yml` file with the correct configuration.
3. Go into the `deployment` directory and run the command:

```bash
docker compose up -d
```

This will pull images from my docker hub repo and run them in the background.

Note: we can check the status of each container using the following command:

```bash
docker ps
```

4. Once the containers are all running, you can follow along in the next section.

### Things we can do

#### Storing Data

We can send POST requests to the receiver service to store events. There are 2 endpoints that we can hit.

1. New Item Transaction (POST)

URL: `http://<ip-address>:8080/new/item_transaction`

Body:
```json
{
  "transaction_id": "ed90a56d-fc89-4112-9dee-dd31fe9d55d9",
  "item_id": "8346cd90-aac9-4241-a644-1b2349ea505e",
  "user_id": "f33ce732-958d-4894-bacd-91512eecf3df",
  "transaction_date": "2024-02-05T12:31:10.001000+00:00",
  "item_price": 10
}
```

2. New Gun Stat (POST)

URL: `http://<ip-address>:8080/new/gun_stat`

Body: 
```json
{
  "gun_id": "d290f1ee-6c54-4b01-90e6-d701748f0851",
  "game_id": "1c3b5a4e-b4d3-42f9-afaa-b3618924bbe2",
  "user_id": "736bf87e-79e5-4d49-8e52-8e75d5e06f84",
  "num_missed_shots": 300,
  "num_body_shots": 800,
  "num_head_shots": 2121,
  "num_bullets_shot": 300
}
```

#### Viewing Data

Once there is data stored in the database, we can also view the data. The `Dashboard` service is a single web page application that will display some stats, calculated based on the stored data in the database, and some random data stored in the database.

URL: `http://<ip-address>:3000`

# Running Services

### Zookeeper Service

hostname: zookeeper
port: 2181

### Kafka Service

hostname: kafka
port: 9092

### MySQL DB Service

hostname: db
port: 8090

### Audit Service

hostname: audit_log
port: 8110

### Receiver Service

hostname: receiver
port: 8080

### Storage Service

hostname: storage
port: 8090

### Processing Service

hostname: processing
port: 8100

### Dashboard Service

hostname: dashboard
port: 3000

# SQL Commands

### Getting a specific index

`SELECT * FROM gun_stats WHERE id=1;`

`SELECT * FROM purchase_history WHERE id=1;`
