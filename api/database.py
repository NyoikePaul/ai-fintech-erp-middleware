from sqlalchemy import create_all, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:pass@db:5432/biashara")

Base = declarative_base()

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    receipt_number = Column(String, unique=True, index=True)
    amount = Column(Float)
    phone_number = Column(String)
    checkout_request_id = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

# Note: You'll need to run Base.metadata.create_all(engine) elsewhere 
# or use Alembic migrations for production.
