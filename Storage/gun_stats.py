from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from base import Base


class GunStats(Base):
    """ Gun Stats """

    __tablename__ = "gun_stats"

    id = Column(Integer, primary_key=True)
    trace_id = Column(String(250), nullable=False)
    game_id = Column(String(250), nullable=False)
    gun_id = Column(String(250), nullable=False)
    user_id = Column(String(250), nullable=False)
    num_bullets_shot = Column(Integer, nullable=False)
    num_body_shots = Column(Integer, nullable=False)
    num_head_shots = Column(Integer, nullable=False)
    num_missed_shots = Column(Integer, nullable=False)
    date_created = Column(DateTime, nullable=False)

    def __init__(self, trace_id, game_id, gun_id, user_id, num_bullets_shot, num_body_shots, num_head_shots, num_missed_shots):
        self.trace_id = trace_id
        self.game_id = game_id
        self.gun_id = gun_id
        self.user_id = user_id
        self.num_bullets_shot = num_bullets_shot
        self.num_body_shots = num_body_shots
        self.num_head_shots = num_head_shots
        self.num_missed_shots = num_missed_shots
        self.date_created = datetime.now()

    def to_dict(self):
        dict = {}

        dict['id'] = self.id
        dict['trace_id'] = self.trace_id
        dict['game_id'] = self.game_id
        dict['gun_id'] = self.gun_id
        dict['user_id'] = self.user_id
        dict['date_created'] = self.date_created
        dict['num_bullets_shot'] = self.num_bullets_shot
        dict['num_body_shots'] = self.num_body_shots
        dict['num_head_shots'] = self.num_head_shots
        dict['num_missed_shots'] = self.num_missed_shots

        return dict
