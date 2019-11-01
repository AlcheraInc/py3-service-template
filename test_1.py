#!/usr/bin/env python3
#
# References
#   https://grpc.github.io/docs/tutorials/basic/python.html
#
import pytest

import grpc
import asyncio
import logging
from concurrent import futures

from service import start_secure_serve, remote, read_from_file
from client import create_dir

logging.info("service address: {}".format(remote))

# read in the certificate and create credentials
creds = grpc.ssl_channel_credentials(
    root_certificates=read_from_file('server.crt'))
logging.info("test credentials: {}".format(creds))

# start a service
executor = futures.ThreadPoolExecutor(max_workers=5)
start_secure_serve(remote, executor, 'server.key', 'server.crt')


@pytest.mark.asyncio
async def test_create_dir():
    with grpc.secure_channel(remote, creds) as channel:
        res = await create_dir(channel)

        logging.debug("create_dir: {} {} {}".format(
            res.err, res.message, res.ipath
        ))
        assert res.err == 0
        # assert len(res.ipath) > 0
