import socket
import unittest

from uprotocol.proto.uri_pb2 import UEntity, UUri, UAuthority, UResource
from uprotocol.uri.factory.uresource_builder import UResourceBuilder
from uprotocol.uri.serializer.microuriserializer import MicroUriSerializer
from uprotocol.uri.validator.urivalidator import UriValidator

uri = UUri(entity=UEntity(id=29999, version_major=254), resource=UResource(id=19999))
bytes_uuri = MicroUriSerializer().serialize(uri)
uri2 = MicroUriSerializer().deserialize(bytes_uuri)
print(uri)
print(uri2)