#!/bin/bash
workdir=${2:-"$(pwd)"}

python -m grpc_tools.protoc \
    -I"${workdir}" ${1:-"service.proto"} \
    --python_out="${workdir}" --grpc_python_out="${workdir}";

date
