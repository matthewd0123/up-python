# -------------------------------------------------------------------------

# Copyright (c) 2023 General Motors GTO LLC
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
# SPDX-FileType: SOURCE
# SPDX-FileCopyrightText: 2023 General Motors GTO LLC
# SPDX-License-Identifier: Apache-2.0

# -------------------------------------------------------------------------

import re
import socket

from uprotocol.proto.uri_pb2 import UUri, UAuthority, UEntity
from uprotocol.proto.uri_pb2 import UResource

from uprotocol.uri.serializer.ipaddress import IpAddress
from uprotocol.uri.serializer.uriserializer import UriSerializer
from uprotocol.uri.validator.urivalidator import UriValidator
from uprotocol.uri.factory.uresource_builder import UResourceBuilder

class ShortUriSerializer(UriSerializer):
    """
    UUri Serializer that serializes a UUri to a Short format string per
    https://github.com/eclipse-uprotocol/uprotocol-spec/blob/main/basics/uri.adoc
    """

    def serialize(self, uri: UUri) -> bytes:
        if uri is None or UriValidator.is_empty(uri):
            return ""
    
        sb = []

        if uri.authority is not None:
            authority = uri.authority
            if uri.authority.HasField('ip'):
                try:
                    sb.append("/")
                    sb.append(socket.inet_ntoa(authority.ip))
                except:
                    return ""
            elif uri.authority.HasField('id'):
                sb.append("//")
                sb.append(authority.id.decode("utf-8"))
            else:
                return ""
        
        sb.append("/")
        sb.append(ShortUriSerializer.build_software_entity_part_of_uri(uri.entity))
        sb.append(ShortUriSerializer.build_resource_part_of_uri(uri))

        return re.sub('/+$', '', "".join(sb))
    
    @staticmethod
    def build_resource_part_of_uri(uri):
        if uri.resource is None:
            return ""
        
        resource = uri.resource

        sb = []
        sb.append(resource.id)

        return "".join(sb)

    @staticmethod
    def build_software_entity_part_of_uri(entity):
        """
        Create the service part of the uProtocol URI from an  software entity object.
        @param use  Software Entity representing a service or an application.
        """
        sb = []
        sb.append(entity.id)
        sb.append("/")
        if entity.version_major > 0:
            sb.append(entity.version_major)
        
        return "".join(sb)

    def deserialize(uprotocol_uri):
        """
        Deserialize a String into a UUri object.
        @param uProtocolUri A short format uProtocol URI.
        @return Returns an UUri data object.
        """
        if uprotocol_uri is None or uprotocol_uri.strip() == "":
            return UUri()
        
        uri = uprotocol_uri[uprotocol_uri.index(":")+1:] if ":" in uprotocol_uri else uprotocol_uri.replce("\\", "/")

        is_local = not uprotocol_uri.startswith("//")

        uri_parts = uri.split("/")
        number_of_parts_in_uri = len(uri_parts)

        if number_of_parts_in_uri < 2:
            return UUri()
        
        ue_id = ""
        ue_version = ""

        resource = None
        authority = None

        if is_local:
            ue_id = uri_parts[1]
            if number_of_parts_in_uri > 2:
                ue_version = uri_parts[2]

                if number_of_parts_in_uri > 3:
                    uresource = ShortUriSerializer.parse_from_string(uri_parts[3])

                if number_of_parts_in_uri > 4:
                    return UUri()
        else:
            if uri_parts[2].strip() == "":
                return UUri()
            
        if IpAddress.is_valid(uri_parts[2]):
            authority = UAuthority(ip=IpAddress.to_bytes(uri_parts[2]))
        else:
            authority = UAuthority(ip=IpAddress.to_bytes(uri_parts[2]))

        if len(uri_parts) > 3:
            ue_id = uri_parts[3]
            if number_of_parts_in_uri > 4:
                ue_version = uri_parts[4]
                if number_of_parts_in_uri > 5:
                    uresource = ShortUriSerializer.parse_from_string(uri_parts[5])
                if number_of_parts_in_uri > 6:
                    return UUri()
        else:
            return UUri(authority=authority)

        ue_version_int = None
        ue_id_int = None

        try:
            if ue_version.strip() != "":
                ue_version_int = int(ue_version)
            if ue_id.strip() != "":
                ue_id_int = int(ue_id)
        except:
            return UUri()
        
        entity = UEntity()

        if ue_id_int is not None:
            entity.id = ue_id_int
        if ue_version_int is not None:
            entity.version_major = ue_version_int
        
        new_uri = UUri()
        new_uri.entity.CopyFrom(entity)

        if authority is not None:
            new_uri.authority.CopyFrom(authority)

        if resource is not None:
            new_uri.resource.CopyFrom(resource)
        
    @staticmethod
    def parse_from_string(resource_string):
        """
        Static factory method for creating a UResource using a string value 
        @param resource_string String that contains the UResource id.
        @return Returns a UResource object.
        """
        if resource_string is None:
            raise ValueError(" Resource must have a command name")
        id = None
        try:
            id = int(resource_string)
        except:
            return UResource()
        
        return UResourceBuilder.from_id(id)