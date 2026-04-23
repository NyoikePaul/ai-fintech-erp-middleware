# Project Automation for Expert Middleware

.PHONY: help install dev test docker-up docker-down

help:
@echo "Available commands:"
@echo "  make install    - Install dependencies"
@echo "  make dev        - Run FastAPI development server"
@echo "  make test       - Run pytest suite"
@echo "  make docker-up  - Start services via Docker Compose"
@echo "  make docker-down - Stop Docker services"

install:
pip install -r requirements.txt

dev:
uvicorn api.main:app --reload

test:
pytest tests/

docker-up:
docker-compose up -d

docker-down:
docker-compose down
