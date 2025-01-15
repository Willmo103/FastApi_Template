# app/models/api_key.py

from sqlalchemy import Column, Integer, String
from app.core.database import Base

class APIKey(Base):
    __tablename__ = "api_keys"

    id = Column(Integer, primary_key=True, index=True)
    key = Column(String, unique=True, index=True, nullable=False)
    owner = Column(String, index=True, nullable=False)
