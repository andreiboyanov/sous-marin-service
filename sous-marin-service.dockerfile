FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /app

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | \
    POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock /app/
RUN poetry install
COPY ./sous_marin /app
ENV PYTHONPATH=/sous_marin