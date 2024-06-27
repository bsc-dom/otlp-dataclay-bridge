#!/bin/bash

python3 -m grpc_tools.protoc \
  --proto_path=opentelemetry-proto/ \
  --python_out=./ \
  --grpc_python_out=./ \
  opentelemetry-proto/opentelemetry/proto/common/v1/*.proto \
  opentelemetry-proto/opentelemetry/proto/collector/logs/v1/*.proto \
  opentelemetry-proto/opentelemetry/proto/collector/metrics/v1/*.proto \
  opentelemetry-proto/opentelemetry/proto/logs/v1/*.proto \
  opentelemetry-proto/opentelemetry/proto/metrics/v1/*.proto \
  opentelemetry-proto/opentelemetry/proto/resource/v1/*.proto \
