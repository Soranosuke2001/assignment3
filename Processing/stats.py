from sqlalchemy import Column, Integer, DateTime
from base import Base
from datetime import datetime

class Stats(Base):
    """ Stats Table """

    __tablename__ = "stats"

    id = Column(Integer, primary_key=True)
    num_gun_stat_events = Column(Integer, nullable=False)
    head_shot_count = Column(Integer, nullable=False)
    bullet_shot_count = Column(Integer, nullable=False)
    num_purchase_history_events = Column(Integer, nullable=False)
    total_revenue = Column(Integer, nullable=False)
    last_updated = Column(DateTime, nullable=False)

    def __init__(self, num_gun_stat_events, head_shot_count, bullet_shot_count, num_purchase_history_events, total_revenue, last_updated):
        self.num_gun_stat_events = num_gun_stat_events
        self.head_shot_count = head_shot_count
        self.bullet_shot_count = bullet_shot_count
        self.num_purchase_history_events = num_purchase_history_events
        self.total_revenue = total_revenue
        self.last_updated = last_updated

    def to_dict(self):
        dict = {}

        dict['num_gun_stat_events'] = self.num_gun_stat_events
        dict['head_shot_count'] = self.head_shot_count
        dict['bullet_shot_count'] = self.bullet_shot_count
        dict['num_purchase_history_events'] = self.num_purchase_history_events
        dict['total_revenue'] = self.total_revenue
        dict['last_updated'] = self.last_updated

        return dict
