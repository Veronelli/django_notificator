FROM python:slim-bookworm

RUN pip install poetry virtualenv

WORKDIR /usr/src/app/

COPY ./pyproject.toml .

RUN python3 -m venv .venv &&\
    . .venv/bin/activate &&\
    poetry install

