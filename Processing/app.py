import time
from datetime import datetime
import connexion
from connexion.middleware import MiddlewarePosition
from starlette.middleware.cors import CORSMiddleware
from apscheduler.schedulers.background import BackgroundScheduler
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from base import Base
from stats import Stats

from helpers.log_message import start_request, end_request, data_found, data_not_found, start_periodic, end_periodic, updated_db, no_events
from helpers.query_database import row_counter, check_db, update_storage
from helpers.read_config import get_sqlite_config, read_log_config

filename, seconds, url = get_sqlite_config()
logger = read_log_config()

DB_ENGINE = create_engine(f"sqlite:///{filename}")
Base.metadata.bind = DB_ENGINE
DB_SESSION = sessionmaker(bind=DB_ENGINE)


def get_stats():
    start_request(logger)

    session = DB_SESSION()

    response = row_counter(session, Stats)

    session.close()

    if response is None:
        data_not_found(logger, 400, "No new data")

        return "No Data Found", 400

    data_found(logger, response)
    end_request(logger)

    return response, 200


def populate_stats():
    start_periodic(logger)

    session = DB_SESSION()

    data = check_db(session, Stats)

    new_data = update_storage(logger, data)

    if new_data == "error":
        return

    if new_data['new_event']:
        updated_db(logger, new_data)
    else:
        last_updated = datetime.now()
        new_data['last_updated'] = last_updated

        no_events(logger, last_updated.strftime("%Y-%m-%d %H:%M:%S.%f"))

    pr = Stats(
        new_data['num_gun_stat_events'],
        new_data['head_shot_count'],
        new_data['bullet_shot_count'],
        new_data['num_purchase_history_events'],
        new_data['total_revenue'],
        new_data['last_updated'],
    )

    session.add(pr)

    session.commit()
    session.close()

    end_periodic(logger)


def init_scheduler():
    sched = BackgroundScheduler(daemon=True)
    sched.add_job(populate_stats, 'interval', seconds=seconds)

    sched.start()


app = connexion.FlaskApp(__name__, specification_dir='')
app.add_middleware(CORSMiddleware, position=MiddlewarePosition.BEFORE_EXCEPTION, allow_origins=[
                   "*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.add_api("./config/openapi.yml",
            strict_validation=True, validate_response=True)

if __name__ == "__main__":
    time.sleep(20)

    init_scheduler()
    app.run(host="0.0.0.0", port=8100)
