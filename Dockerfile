FROM python:3.13.3-slim

WORKDIR /app

COPY ./src /app/src
COPY ./pyproject.toml /app/pyproject.toml

RUN python -m pip install -e .

ENTRYPOINT ["dev2il-devops-app"]
