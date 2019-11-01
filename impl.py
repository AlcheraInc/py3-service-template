
import logging
import os
from os.path import join, isdir, isfile, islink, abspath

import service_pb2
import service_pb2_grpc


class Basic(service_pb2_grpc.VolumeServicer):
    def Create1(self, request: service_pb2.Request, context) -> service_pb2.Response:
        logging.info('Create1')
        return service_pb2.Response()

    def Create2(self, request_iterator, context):
        logging.info('Create2')
        for _ in request_iterator:
            yield service_pb2.Response()

    def Remove(self, request: service_pb2.Request, context) -> service_pb2.Response:
        logging.info('Remove')
        return service_pb2.Response()

    def List(self, request: service_pb2.Request, context):
        logging.info('List')
        yield service_pb2.Response()
        yield service_pb2.Response()

    def Exists(self, request_iterator, context) -> service_pb2.Response:
        logging.info('Exists')
        for _ in request_iterator:
            continue
        return service_pb2.Response()
