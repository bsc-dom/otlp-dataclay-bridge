FROM python:3.11

COPY requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY ./opentelemetry /usr/src/app/opentelemetry
COPY ./model /usr/src/app/model
COPY ./run_bridge.py /usr/src/app

CMD ["python", "-U", "run_bridge.py"]
