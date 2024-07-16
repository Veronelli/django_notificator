FROM python:slim-bookworm

RUN pip install poetry virtualenv

WORKDIR /usr/src/app/

COPY . .

RUN virtualenv /opt/.venv && \
    . /opt/.venv/bin/activate && \
    poetry install 

CMD ["/bin/bash", "cmd.sh"]