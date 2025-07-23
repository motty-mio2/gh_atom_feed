FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim AS req

WORKDIR /io

RUN --mount=type=bind,source=./pyproject.toml,target=/io/pyproject.toml \
    --mount=type=bind,source=./uv.lock,target=/io/uv.lock \
    uv export --no-dev --no-hashes --no-emit-project --output-file /requirements.txt

FROM python:3.11-slim-bookworm AS base

RUN --mount=type=bind,from=req,source=/requirements.txt,target=/requirements.txt \
    pip install --no-cache-dir -r /requirements.txt


WORKDIR /app
ENV PYTHONPATH="/app/src/" \
    PORT=8080

COPY ./src /app/src

RUN --mount=type=bind,source=./pyproject.toml,target=/app/pyproject.toml \
    --mount=type=bind,source=./README.md,target=/app/README.md \
    pip install --no-cache-dir /app


CMD ["python", "-m", "fastapi", "run", "/app/src/gh_atom_feed/main.py", "--port", "${PORT}"]
EXPOSE "${PORT}"
