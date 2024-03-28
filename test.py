import json
import os
import unittest

from uprotocol.uri.serializer.longuriserializer import LongUriSerializer
from uprotocol.uri.validator.urivalidator import UriValidator
from uprotocol.uri.factory.uresource_builder import UResourceBuilder
from uprotocol.validation.validationresult import ValidationResult
from uprotocol.proto.uri_pb2 import UUri, UEntity, UResource, UAuthority


UriValidator.is_local(None)