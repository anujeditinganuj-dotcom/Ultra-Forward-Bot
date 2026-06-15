FROM python:3.10-slim

RUN apt-get update && apt-get install -y git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /requirements.txt

RUN pip install --upgrade pip && pip install -r /requirements.txt

WORKDIR /fwdbot
COPY . /fwdbot

CMD ["bash", "start.sh"]
