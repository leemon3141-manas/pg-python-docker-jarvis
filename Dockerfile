FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install psycopg[binary] faker

CMD ["python", "main.py"]
