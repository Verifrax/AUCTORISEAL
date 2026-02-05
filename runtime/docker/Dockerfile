FROM python:3.11-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1

COPY . /app

RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt || true

EXPOSE 8080

ENTRYPOINT ["/app/runtime/docker/entrypoint.sh"]
