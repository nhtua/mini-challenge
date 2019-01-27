from sqlalchemy import Column, Integer, TIMESTAMP, String, Date
from model.database import Base


class User(Base):
    __tablename__ = 'user'
    id         = Column(Integer, primary_key=True, autoincrement=True)
    username   = Column(String(64))
    password   = Column(String(64))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
