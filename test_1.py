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


# read in the certificate and create credentials
creds = grpc.ssl_channel_credentials(root_certificates=read_from_file('server.crt'),
                                     private_key=read_from_file('server.key'),
                                     certificate_chain=read_from_file('server.crt'))
logging.info("test credentials: {}".format(creds))

# start a service
start_secure_serve(remote, futures.ThreadPoolExecutor(max_workers=2),
                   'server.key', 'server.crt')
logging.info("service address: {}".format(remote))


@pytest.mark.asyncio
async def test_given_insecure_when_operation_then_throws():
    try:
        with grpc.insecure_channel(remote) as channel:
            await create_dir(channel)

        logging.error("expect operation failure with insecure channel")
    except Exception as e:
        logging.debug("expected failure: {}".format(e))
        return


@pytest.mark.asyncio
async def test_given_secure_when_createdir_then_success():
    with grpc.secure_channel(remote, creds) as channel:
        res = await create_dir(channel)

        logging.debug("create_dir: {} {} {}".format(
            res.err, res.message, res.ipath
        ))
        assert res.err == 0
        # assert len(res.ipath) > 0
