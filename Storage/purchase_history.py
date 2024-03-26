from sqlalchemy import Column, Integer, String, DateTime
from base import Base
from datetime import datetime

class PurchaseHistory(Base):
    """ Item Purchase History """

    __tablename__ = "purchase_history"

    id = Column(Integer, primary_key=True)
    trace_id = Column(String(250), nullable=False)
    transaction_id = Column(String(250), nullable=False)
    item_id = Column(String(250), nullable=False)
    user_id = Column(String(250), nullable=False)
    item_price = Column(Integer, nullable=False)
    transaction_date = Column(String(100), nullable=False)
    date_created = Column(DateTime, nullable=False)

    def __init__(self, trace_id, transaction_id, item_id, user_id, item_price, transaction_date):
        self.trace_id = trace_id
        self.transaction_id = transaction_id
        self.item_id = item_id
        self.user_id = user_id
        self.item_price = item_price
        self.transaction_date = transaction_date
        self.date_created = datetime.now()

    def to_dict(self):
        dict = {}

        dict['id'] = self.id
        dict['trace_id'] = self.trace_id
        dict['transaction_id'] = self.transaction_id
        dict['item_id'] = self.item_id
        dict['user_id'] = self.user_id
        dict['item_price'] = self.item_price
        dict['transaction_date'] = self.transaction_date
        dict['date_created'] = self.date_created

        return dict