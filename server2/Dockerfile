FROM python:3.11-slim

WORKDIR /app


COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt



COPY . .


RUN mkdir -p /app/db


EXPOSE 8002


CMD ["uvicorn", "main:app", "--host", "localhost", "--port", "8002"]
