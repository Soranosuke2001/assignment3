from pykafka import KafkaClient
from pykafka.protocol import Message
import json

from logging import Logger


def log_debug(logger: Logger, event_name, trace_id):
    logger.debug(f"Stored event {event_name} request with a trace id of {trace_id}")


def kafka_fetch(kafka_hostname, kafka_port, kafka_topic, event_type, index, logger: Logger):
    client = KafkaClient(hosts=f'{kafka_hostname}:{kafka_port}')
    topic = client.topics[str.encode(kafka_topic)]

    consumer = topic.get_simple_consumer(
        reset_offset_on_start=True, 
        consumer_timeout_ms=3000
    )

    try:
        count = 0
        test_count = 0
        
        msg: Message

        for msg in consumer:
            msg_str = msg.value.decode('utf-8')
            message = json.loads(msg_str)

            test_count += 1


            if message["type"] == event_type:
                if count == index:
                    return message["payload"], 200

                count += 1
    except:
        logger.error("No more messages found...")
    finally:
        print(test_count)

    logger.error(f"Could not find {event_type} at index: {index}")

    return { "message": "Not Found" }, 404
