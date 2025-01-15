# app/schemas/api_key.py

from pydantic import BaseModel

class APIKeyCreate(BaseModel):
    owner: str

class APIKeyResponse(BaseModel):
    key: str

    class Config:
        orm_mode = True
