from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # App Config
    API_BASE_URL: str = "https://api.yourdomain.com"
    DATABASE_URL: str = "postgresql://user:pass@localhost:5432/biashara_db"
    
    # M-Pesa (Daraja)
    MPESA_CONSUMER_KEY: str
    MPESA_CONSUMER_SECRET: str
    MPESA_PASSKEY: str
    MPESA_SHORTCODE: str = "174379"
    MPESA_BASE_URL: str = "https://sandbox.safaricom.co.ke"

    # Odoo
    ODOO_URL: str
    ODOO_DB: str
    ODOO_USERNAME: str
    ODOO_PASSWORD: str

    # AI
    OPENAI_API_KEY: str

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()
