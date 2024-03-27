import uuid
import time
import connexion
from pykafka import KafkaClient
from connexion import NoContent

from helpers.read_config import get_urls, read_log_config, get_kafka_config, get_flask_config
from helpers.kafka_message import kafka_message

gun_stat_url, item_transaction_url = get_urls()
kafka_hostname, kafka_port, kafka_topic = get_kafka_config()
flask_host, flask_port = get_flask_config()
logger = read_log_config()

time.sleep(10)

CONNECTED = False

while not CONNECTED:
    try:
        client = KafkaClient(hosts=f'{kafka_hostname}:{kafka_port}')
        topic = client.topics[str.encode(kafka_topic)]
        producer = topic.get_sync_producer()
        CONNECTED = True
    except:
        logger.error("Failed to connect to Kafka, retrying in 5 seconds")
        time.sleep(5)


def create_gun_stat(body):
    trace_id = gen_trace_id()
    body['trace_id'] = trace_id

    log_message(trace_id, "create_gun_stat", "receive")

    kafka_message(producer, body, "gun_stat")

    log_message(trace_id, "create_gun_stat", "return", 201)

    return NoContent, 201


def create_purchase_transaction(body):
    trace_id = gen_trace_id()
    body['trace_id'] = trace_id

    log_message(trace_id, "create_purchase_transaction", "receive")

    kafka_message(producer, body, "purchase_history")

    log_message(trace_id, "create_purchase_transaction", "return", 201)

    return NoContent, 201


def gen_trace_id():
    return str(uuid.uuid4())


def log_message(trace_id, event_name, event, status_code=400):
    if event == "receive":
        logger.info(f"Received event {event_name} request with a trace id of {trace_id}")
    else:
        logger.info(f"Returned event {event_name} response ID: {trace_id} with status {status_code}")


app = connexion.FlaskApp(__name__, specification_dir='')
app.add_api("./config/openapi.yml",
            strict_validation=True, validate_response=True)


if __name__ == "__main__":
    app.run(host=flask_host, port=flask_port)
