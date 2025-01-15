# app/utils/api_key_generator.py

import secrets

def generate_api_key() -> str:
    return secrets.token_urlsafe(32)
