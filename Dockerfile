
FROM python:3.11-slim

WORKDIR /app

COPY . .

ENV PYTHONUNBUFFERED=1

RUN pip install --no-cache-dir ldap3

ENTRYPOINT ["python", "main.py"]
