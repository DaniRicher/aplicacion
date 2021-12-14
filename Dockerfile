FROM python:3.9.7-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY poetry.lock /usr/src/app
COPY pyproject.toml /usr/src/app

RUN set -eux \
    && apk add --no-cache --virtual .build-deps build-base \
    libressl-dev libffi-dev gcc musl-dev python3-dev \
    && pip3 install --upgrade pip \
    && pip3 install poetry && poetry config virtualenvs.create false \
    && poetry install --no-dev


RUN poetry config virtualenvs.create false && poetry install

COPY . /usr/src/app   
CMD ["uvicorn","app.main:app","--reload","--workers","1","--host","0.0.0.0","--port","8000"]
