FROM python:3.11-rc-bullseye

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app /app/