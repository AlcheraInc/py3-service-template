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

from service import start_serve, remote
from client import create_dir

logging.info("service address: {}".format(remote))
executor = futures.ThreadPoolExecutor(max_workers=5)
start_serve(remote, executor)


@pytest.mark.asyncio
async def test_create_dir():
    with grpc.insecure_channel(remote) as channel:
        res = await create_dir(channel)

        logging.debug("create_dir: {} {} {}".format(
            res.err, res.message, res.ipath
        ))
        assert res.err == 0
        # assert len(res.ipath) > 0
