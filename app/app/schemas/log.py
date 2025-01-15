# app/schemas/log.py

from pydantic import BaseModel
from datetime import datetime

class LogCreate(BaseModel):
    timestamp: datetime
    method: str
    url: str
    headers: str
    body: str
    response_status: int
    response_body: str
