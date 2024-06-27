# OpenTelemetry to dataClay bridge

## Data generation

To test this utility, the `otel/opentelemetry-collector` is used with the `telemetry` service
activated (see `docker-compose.yml` and `otel-config.yaml` for more information). This is ONLY
used for having some dummy sample data so that we can validate that the bridge is receiving and
processing data.

Any proper functional testing (and, of course, a production environment) will have real data and a
proper collector configured instead.

## Preparing a local dataClay environment

A `docker-compose.yml` is provided. Run `docker compose up`.

If you don't want the dummy `otel-collector` container comment it.

## Bridge settings

The bridge expects to find some configuration in dataClay. This allows the system to have some
flexible runtime configuration.

The notebooks include some demo configuration on how they work.

## Running the OTLP-dataClay bridge in a virtual environment

Create the virtual environment and install the requirements (`pip install -r requirements.txt`).

After this, you can run the `run_bridge.py` script directly, i.e.:

```bash
$ ./run_bridge.py
```

# Running the Jupyter Notebook and the full example

**CAUTION!** The default Open Telemetry prometheus port is 8888 and Jupyter Notebook starts to
occupy ports at 8888. I could change default port values, but I was a bit confused and decided to
leave `otel-config.yaml` as vanila as possible (aligned to the typical examples found in the
documentation) so you may need to restart the notebook and restart the otel-collector if you see
errors on docker compose logs.

1. Start the docker compose. Keep it running.
2. Start the Jupyter Notebook. Keep it running.
3. Run the Jupyter Notebook `BridgeConfig` (change settings if you wish)
4. Start the bridge (`run_bridge.py`). Keep it running.
5. Play with the `Consumer` Notebook. If should adapt real time (by default the collector is
   configured to batch every 60 seconds, but that is configurable at the OpenTelemetry
   configuration level and is set as that just to experiment).
