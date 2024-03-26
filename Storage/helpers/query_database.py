from datetime import datetime
from sqlalchemy import and_, func
from sqlalchemy.orm import Session

from gun_stats import GunStats
from purchase_history import PurchaseHistory


def convert_datetime(timestamp):
    return datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")


def fetch_timestamp_results(start_timestamp, end_timestamp, session: Session, table: GunStats | PurchaseHistory):
    start_datetime = convert_datetime(start_timestamp)
    end_datetime = convert_datetime(end_timestamp)

    results = session.query(table).filter(and_(table.date_created > start_datetime, table.date_created <= end_datetime)).all()

    result_formatted = []

    for result in results:
        result_formatted.append(result.to_dict())
    
    return result_formatted


def fetch_row_count(session: Session, table):
    row_count = session.query(func.count(table.id)).scalar()

    return row_count