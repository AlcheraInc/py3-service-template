#!/usr/bin/env python3
#
# References
#   https://grpc.github.io/docs/tutorials/basic/python.html
#
# Usage
#   service.py ${service_address}
#
import grpc
import service_pb2_grpc
import impl

from concurrent import futures
import os
import sys
import logging
import asyncio


def make_service(thread_pool: futures.ThreadPoolExecutor) -> grpc.Server:
    launcher = grpc.server(thread_pool)
    # you can register multiple service to 1 launcher
    service = impl.Basic()
    service_pb2_grpc.add_VolumeServicer_to_server(service, launcher)
    return launcher


def start_serve(remote: str, thread_pool: futures.ThreadPoolExecutor) -> grpc.Server:
    launcher = make_service(thread_pool)
    # todo: add_secure_port
    launcher.add_insecure_port(remote)
    launcher.start()
    return launcher


def read_from_file(fpath: str):
    with open(fpath, 'rb') as f:
        return f.read()


def start_secure_serve(remote: str, thread_pool: futures.ThreadPoolExecutor,
                       key_path: str = 'server.key', cert_path: str = 'server.pem') -> grpc.Server:
    # generate credential with the key and certificate
    key_data = read_from_file(key_path)
    cert_chain = read_from_file(cert_path)
    creds = grpc.ssl_server_credentials(((key_data, cert_chain,),))

    # create server with credentials
    launcher = make_service(thread_pool)
    launcher.add_secure_port(remote, creds)
    launcher.start()
    return launcher


async def serve(remote: str, thread_pool: futures.ThreadPoolExecutor):
    launcher = start_serve(remote, thread_pool)
    await launcher.wait_for_termination()


remote = 'localhost:9090'

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        remote = sys.argv[1]
    logging.info("service address: {}".format(remote))
    executor = futures.ThreadPoolExecutor(max_workers=5)

    asyncio.get_event_loop().run_until_complete(
        serve(remote, executor)
    )
