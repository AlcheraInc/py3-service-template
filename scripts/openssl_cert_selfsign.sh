#!/bin/bash

bash ./scripts/gen_cert_info.sh ${3:-"localhost"} ${4:-"dh.park@alcherainc.com"} | \
openssl req -new -x509 \
    -sha256 \
    -key ${1:-"server.key"} \
    -out ${2:-"server.crt"} -days 30 2> /dev/null
