import hmac

from fastapi.security import APIKeyHeader
from fastapi import HTTPException, Security

from core.config import X_API_KEY

api_key_header = APIKeyHeader(name="X-API-Key")

async def verify_api_key(api_key: str = Security(api_key_header)):
    if not X_API_KEY:
        raise HTTPException(
            status_code=503,
            detail="API key is not configured.",
        )
    if not hmac.compare_digest(api_key, X_API_KEY):
        raise HTTPException(
            status_code=401,
            detail="API key tidak valid.",
        )
    return api_key