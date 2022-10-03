FROM python:3.11-rc-bullseye

WORKDIR /erdos

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app /erdos/app