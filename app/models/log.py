# app/models/log.py

from sqlalchemy import Column, Integer, String, DateTime, Text
from app.core.database import Base
from datetime import datetime

class Log(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    method = Column(String, nullable=False)
    url = Column(String, nullable=False)
    headers = Column(Text, nullable=True)
    body = Column(Text, nullable=True)
    response_status = Column(Integer, nullable=False)
    response_body = Column(Text, nullable=True)
