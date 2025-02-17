FROM python:3.11

COPY requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt

RUN mkdir -p /dataclay/storage; \
    mkdir -p /dataclay/metadata

WORKDIR /usr/src
