# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: uri.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\turi.proto\x12\x0cuprotocol.v1\"\x85\x01\n\x04UUri\x12+\n\tauthority\x18\x01 \x01(\x0b\x32\x18.uprotocol.v1.UAuthority\x12%\n\x06\x65ntity\x18\x02 \x01(\x0b\x32\x15.uprotocol.v1.UEntity\x12)\n\x08resource\x18\x03 \x01(\x0b\x32\x17.uprotocol.v1.UResource\"N\n\nUAuthority\x12\x11\n\x04name\x18\x01 \x01(\tH\x01\x88\x01\x01\x12\x0c\n\x02ip\x18\x02 \x01(\x0cH\x00\x12\x0c\n\x02id\x18\x03 \x01(\x0cH\x00\x42\x08\n\x06numberB\x07\n\x05_name\"\x8b\x01\n\x07UEntity\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x02id\x18\x02 \x01(\rH\x00\x88\x01\x01\x12\x1a\n\rversion_major\x18\x03 \x01(\rH\x01\x88\x01\x01\x12\x1a\n\rversion_minor\x18\x04 \x01(\rH\x02\x88\x01\x01\x42\x05\n\x03_idB\x10\n\x0e_version_majorB\x10\n\x0e_version_minor\"w\n\tUResource\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\x08instance\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x14\n\x07message\x18\x03 \x01(\tH\x01\x88\x01\x01\x12\x0f\n\x02id\x18\x04 \x01(\rH\x02\x88\x01\x01\x42\x0b\n\t_instanceB\n\n\x08_messageB\x05\n\x03_id\"-\n\tUUriBatch\x12 \n\x04uris\x18\x01 \x03(\x0b\x32\x12.uprotocol.v1.UUriB\'\n\x18org.eclipse.uprotocol.v1B\tUUriProtoP\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'uri_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030org.eclipse.uprotocol.v1B\tUUriProtoP\001'
  _UURI._serialized_start=28
  _UURI._serialized_end=161
  _UAUTHORITY._serialized_start=163
  _UAUTHORITY._serialized_end=241
  _UENTITY._serialized_start=244
  _UENTITY._serialized_end=383
  _URESOURCE._serialized_start=385
  _URESOURCE._serialized_end=504
  _UURIBATCH._serialized_start=506
  _UURIBATCH._serialized_end=551
# @@protoc_insertion_point(module_scope)