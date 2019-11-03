#!/usr/bin/env python3
#
# References
#   https://grpc.github.io/docs/tutorials/basic/python.html
#
import grpc
import asyncio
import logging

import service_pb2
import service_pb2_grpc


async def create_dir(channel: grpc.Channel, dirpath: str, force: bool = False):
    await asyncio.sleep(0)
    stub = service_pb2_grpc.VolumeStub(channel)
    req = service_pb2.Request()
    req.itype, req.dirpath, req.force = 'dir', dirpath, force
    return stub.Create1(req)
