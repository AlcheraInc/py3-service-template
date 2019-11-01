# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='service.proto',
  package='smp',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\rservice.proto\x12\x03smp\"U\n\x07Request\x12\r\n\x05itype\x18\x01 \x01(\t\x12\x0c\n\x04perm\x18\x02 \x01(\r\x12\x0f\n\x07\x64irpath\x18\x03 \x01(\t\x12\r\n\x05\x66name\x18\x04 \x01(\t\x12\r\n\x05\x66orce\x18\x05 \x01(\x08\"7\n\x08Response\x12\x0b\n\x03\x65rr\x18\x01 \x01(\r\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\r\n\x05ipath\x18\x03 \x01(\t2\xde\x01\n\x06Volume\x12(\n\x07\x43reate1\x12\x0c.smp.Request\x1a\r.smp.Response\"\x00\x12,\n\x07\x43reate2\x12\x0c.smp.Request\x1a\r.smp.Response\"\x00(\x01\x30\x01\x12(\n\x07Remove1\x12\x0c.smp.Request\x1a\r.smp.Response\"\x00\x12\'\n\x04List\x12\x0c.smp.Request\x1a\r.smp.Response\"\x00\x30\x01\x12)\n\x06\x45xists\x12\x0c.smp.Request\x1a\r.smp.Response\"\x00(\x01\x62\x06proto3')
)




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='smp.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='itype', full_name='smp.Request.itype', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='perm', full_name='smp.Request.perm', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dirpath', full_name='smp.Request.dirpath', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fname', full_name='smp.Request.fname', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='force', full_name='smp.Request.force', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=107,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='smp.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err', full_name='smp.Response.err', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='smp.Response.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ipath', full_name='smp.Response.ipath', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=109,
  serialized_end=164,
)

DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:smp.Request)
  })
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:smp.Response)
  })
_sym_db.RegisterMessage(Response)



_VOLUME = _descriptor.ServiceDescriptor(
  name='Volume',
  full_name='smp.Volume',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=167,
  serialized_end=389,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create1',
    full_name='smp.Volume.Create1',
    index=0,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Create2',
    full_name='smp.Volume.Create2',
    index=1,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Remove1',
    full_name='smp.Volume.Remove1',
    index=2,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='smp.Volume.List',
    index=3,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Exists',
    full_name='smp.Volume.Exists',
    index=4,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_VOLUME)

DESCRIPTOR.services_by_name['Volume'] = _VOLUME

# @@protoc_insertion_point(module_scope)
