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

logging.info("service address: {}".format(remote))
executor = futures.ThreadPoolExecutor(max_workers=5)
start_serve(remote, executor)


async def print_channel_remote(channel: grpc.Channel):
    await asyncio.sleep(0)
    pass


@pytest.mark.asyncio
async def test_prepare_with_zero_params():
    with grpc.insecure_channel(remote) as channel:
        await print_channel_remote(channel)
