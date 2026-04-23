from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from core.config import settings

# Expert setup: Using HS256 for symmetric encryption
SECRET_KEY = "SUPER_SECRET_CHANGE_ME" 
ALGORITHM = "HS256"

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """Generates a secure JWT for API authentication."""
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str):
    """Decodes and validates a JWT."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
