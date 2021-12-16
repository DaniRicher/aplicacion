#!/bin/bash

# Run migrations
alembic upgrade head

#Start app
#poetry run uvicorn app.main:app --reload --workers 1 --host 0.0.0.0 --port 8000
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload