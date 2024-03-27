import uuid
import time
import connexion
from pykafka import KafkaClient
from connexion import NoContent

"""
This module contains the main application logic for handling requests and interacting with Kafka.
"""

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
    except Exception as e:
        logger.error("Failed to connect to Kafka, retrying in 5 seconds")
        time.sleep(5)


def create_gun_stat(body):
    """
    Create a gun stat record.

    :param body: The request body containing gun stat data.
    :return: Tuple (response body, status code).
    """
    trace_id = gen_trace_id()
    body['trace_id'] = trace_id

    log_message(trace_id, "create_gun_stat", "receive")

    kafka_message(producer, body, "gun_stat")

    log_message(trace_id, "create_gun_stat", "return", 201)

    return NoContent, 201


def create_purchase_transaction(body):
    """
    Create a purchase transaction record.

    :param body: The request body containing transaction data.
    :return: Tuple (response body, status code).
    """
    trace_id = gen_trace_id()
    body['trace_id'] = trace_id

    log_message(trace_id, "create_purchase_transaction", "receive")

    kafka_message(producer, body, "purchase_history")

    log_message(trace_id, "create_purchase_transaction", "return", 201)

    return NoContent, 201


def gen_trace_id():
    """
    Generate a unique trace ID.

    :return: A unique trace ID.
    """
    return str(uuid.uuid4())


def log_message(trace_id, event_name, event, status_code=400):
    """
    Log a message related to an event.

    :param trace_id: The trace ID associated with the event.
    :param event_name: The name of the event.
    :param event: The type of event ("receive" or "return").
    :param status_code: The HTTP status code (default is 400).
    """
    if event == "receive":
        logger.info("Received event %s request with a trace id of %s", event_name, trace_id)
    else:
        logger.info("Returned event %s response ID: %s with status %s", 
                    event_name, trace_id, status_code)


app = connexion.FlaskApp(__name__, specification_dir='')
app.add_api("./config/openapi.yml",
            strict_validation=True, validate_response=True)


if __name__ == "__main__":
    app.run(host=flask_host, port=flask_port)
