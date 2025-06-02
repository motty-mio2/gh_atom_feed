FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim AS req

WORKDIR /io

RUN --mount=type=bind,source=./pyproject.toml,target=/io/pyproject.toml \
    --mount=type=bind,source=./uv.lock,target=/io/uv.lock \
    uv export --no-dev --no-hashes --no-emit-project --output-file /requirements.txt

FROM python:3.11-slim-bookworm AS base

RUN --mount=type=bind,from=req,source=/requirements.txt,target=/requirements.txt \
    pip install --no-cache-dir -r /requirements.txt


WORKDIR /app
ENV PYTHONPATH="/app/src/"

ARG USERNAME=dev \
    UID=1000 \
    GID=1000

RUN groupadd -g "$GID" "$USERNAME" && \
    useradd -l -m -u "$UID" -g "$GID" "$USERNAME"

USER "$USERNAME"

COPY --chown="$USERNAME":"$USERNAME" ./src /app/src

RUN --mount=type=bind,source=./pyproject.toml,target=/app/pyproject.toml \
    --mount=type=bind,source=./README.md,target=/app/README.md \
    pip install --no-cache-dir /app


CMD ["fastapi", "run", "src/gh_atom_feed/main.py", "--port", "8080"]