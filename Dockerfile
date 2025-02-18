FROM python:3.10

COPY requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt

RUN mkdir -p /dataclay/storage; \
    mkdir -p /dataclay/metadata

WORKDIR /usr/src

COPY . /usr/src/app

CMD [ "/usr/local/bin/python3", "/usr/src/app/run_bridge.py" ]
