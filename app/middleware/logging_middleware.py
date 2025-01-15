# app/middleware/logging_middleware.py

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from app.core.database import SessionLocal
from app.models.log import Log
from datetime import datetime
import json

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        db = SessionLocal()
        try:
            # Read request data
            method = request.method
            url = str(request.url)
            headers = dict(request.headers)
            body = await request.body()
            body_str = body.decode('utf-8') if body else ''

            # Process request
            response: Response = await call_next(request)

            # Read response data
            response_body = b""
            async for chunk in response.body_iterator:
                response_body += chunk
            response.body_iterator = iter([response_body])

            response_status = response.status_code
            response_body_str = response_body.decode('utf-8') if response_body else ''

            # Log to database
            log_entry = Log(
                timestamp=datetime.utcnow(),
                method=method,
                url=url,
                headers=json.dumps(headers),
                body=body_str,
                response_status=response_status,
                response_body=response_body_str
            )
            db.add(log_entry)
            db.commit()
        except Exception as e:
            print(f"Logging Middleware Error: {e}")
        finally:
            db.close()

        return response
