# app/routers/api_v1.py

from fastapi import APIRouter, Depends, HTTPException, status
from typing import Dict
from app.schemas.api_key import APIKeyCreate, APIKeyResponse
from app.utils.api_key_generator import generate_api_key
from app.models.api_key import APIKey
from app.core.database import SessionLocal
from sqlalchemy.orm import Session
from app.schemas.log import LogCreate
from app.models.log import Log

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/generate-api-key", response_model=APIKeyResponse)
def create_api_key(api_key: APIKeyCreate, db: Session = Depends(get_db)):
    key = generate_api_key()
    db_api_key = APIKey(key=key, owner=api_key.owner)
    db.add(db_api_key)
    db.commit()
    db.refresh(db_api_key)
    return APIKeyResponse(key=db_api_key.key)

def verify_api_key(db: Session, key: str):
    return db.query(APIKey).filter(APIKey.key == key).first()

@router.get("/test")
def test_endpoint(api_key: str, db: Session = Depends(get_db)):
    db_key = verify_api_key(db, api_key)
    if not db_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"message": "Test endpoint accessed successfully"}

@router.get("/uptime")
def uptime():
    return {"status": "up", "uptime": "24h"}
