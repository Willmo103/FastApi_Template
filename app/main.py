# app/main.py

from fastapi import FastAPI
from app.routers import api_v1
from app.middleware.logging_middleware import LoggingMiddleware
from app.core.config import settings
from app.core.database import Base, engine

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI Template",
    version="1.0.0",
    openapi_url="/api/v1/openapi.json",
    docs_url="/api/v1/docs"
)

# Add middleware
app.add_middleware(LoggingMiddleware)

# Include routers
app.include_router(api_v1.router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Template!"}
