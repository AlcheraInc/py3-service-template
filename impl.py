
import logging
import os
import sys
from os.path import join, isdir, isfile, islink, abspath

import grpc
import service_pb2
import service_pb2_grpc


class Basic(service_pb2_grpc.VolumeServicer):

    @staticmethod
    def remove_file(req: service_pb2.Request) -> int:
        try:
            fpath = os.path.join(req.dirpath, req.fname)
            os.remove(fpath)
            return 0
        except OSError as ex:
            return ex.errno

    @staticmethod
    def remove_dir(req: service_pb2.Request) -> int:
        try:
            os.removedirs(req.dirpath)
            return 0
        except OSError as ex:
            return ex.errno

    @staticmethod
    def create_file(req: service_pb2.Request) -> (str, int):
        try:
            fpath = os.path.join(req.dirpath, req.fname)
            if req.force:
                if isdir(fpath):
                    remove_dir(req)
                else:
                    remove_file(req)
            fd = os.open(fpath, os.O_CREAT | os.O_TRUNC | os.O_RDWR, req.perm)
            return fpath, 0
        except OSError as ex:
            return fpath, ex.errno
        finally:
            if fd > 0:
                os.close(fd)

    @staticmethod
    def create_dir(req: service_pb2.Request) -> int:
        try:
            os.makedirs(req.dirpath, req.perm, req.force)
            return 0
        except OSError as ex:
            return ex.errno

    def Create1(self, req: service_pb2.Request, context) -> service_pb2.Response:
        res = service_pb2.Response()
        if req.itype == 'dir':
            ec = self.create_dir(req)
            if ec != 0:
                context.set_code(grpc.StatusCode.UNAVAILABLE)
                context.set_details(os.strerror(ec))
            else:
                res.ipath = req.dirpath
            return res
        if req.itype == 'file':
            res.ipath, ec = self.create_file(req)
            if ec != 0:
                context.set_code(grpc.StatusCode.UNAVAILABLE)
                context.set_details(os.strerror(ec))
            return res
        context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
        context.set_details("'req.itype' must be one of 'dir' or 'file'")
        return res

    def Create2(self, request_iterator, context):
        for req in request_iterator:
            yield self.Create1(req, context)

    def Remove(self, req: service_pb2.Request, context) -> service_pb2.Response:
        res = service_pb2.Response()
        if req.itype == 'dir':
            ec = self.remove_dir(req)
            if ec != 0:
                context.set_code(grpc.StatusCode.UNAVAILABLE)
                context.set_details(os.strerror(ec))
            return res
        if req.itype == 'file':
            ec = self.remove_file(req)
            if ec != 0:
                context.set_code(grpc.StatusCode.UNAVAILABLE)
                context.set_details(os.strerror(ec))
            return res
        context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
        context.set_details("'req.itype' must be one of 'dir' or 'file'")

        return res

    def List(self, req: service_pb2.Request, context):
        res = service_pb2.Response()
        for _, dirs, files in os.walk(req.dirpath):
            for d in dirs:
                res.ipath = d
                yield res
            for f in files:
                res.ipath = f
                yield res

    def Exists(self, request_iterator, context) -> service_pb2.Response:
        res = service_pb2.Response()
        for req in request_iterator:
            if req.itype == 'dir':
                res.ipath = req.dirpath
                if os.path.exists(res.ipath) == False:
                    return res
                continue
            if req.itype == 'file':
                res.ipath = os.path.join(req.dirpath, req.fname)
                if os.path.exists(res.ipath) == False:
                    return res
                continue
        return service_pb2.Response()
