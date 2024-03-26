import connexion
from connexion.middleware import MiddlewarePosition
from starlette.middleware.cors import CORSMiddleware

from helpers.read_config import read_log_config, get_kafka_config
from helpers.kafka_fetch import kafka_fetch


kafka_hostname, kafka_port, kafka_topic = get_kafka_config()
logger = read_log_config()


def fetch_gun_stat(index):
    logger.info(f"Retrieving Gun Statistic event at index: {index}")

    message, status_code = kafka_fetch(kafka_hostname, kafka_port, kafka_topic, "gun_stat", index, logger)

    return message, status_code


def fetch_purchase_transaction(index):
    logger.info(f"Retrieving Purchase History event at index: {index}")

    message, status_code = kafka_fetch(kafka_hostname, kafka_port, kafka_topic, "purchase_history", index, logger)

    return message, status_code


def log_info(event_type, start_timestamp, end_timestamp, result_len):
    logger.info(f"Query for {event_type} events after {start_timestamp}, until {end_timestamp} return {result_len} results")


app = connexion.FlaskApp(__name__, specification_dir='')
app.add_middleware(CORSMiddleware, position=MiddlewarePosition.BEFORE_EXCEPTION, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.add_api("./config/openapi.yml", strict_validation=True, validate_response=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8110)

