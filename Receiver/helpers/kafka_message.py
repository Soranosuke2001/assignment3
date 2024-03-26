from datetime import datetime
import json


def kafka_message(producer, body, event_type):
    msg = {
        "type": event_type,
        "datetime": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        "payload": body
    }

    msg_str = json.dumps(msg)
    producer.produce(msg_str.encode('utf-8'))

