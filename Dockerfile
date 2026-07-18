
FROM python:3.12-slim

RUN pip install uv


WORKDIR /app

COPY pyproject.toml uv.lock ./


RUN uv sync --frozen --no-dev


COPY . .


EXPOSE 8080

CMD ["sh","c","uv run uvicorn main:app --host 0.0.0.0 --port ${PORT:-8080}"]