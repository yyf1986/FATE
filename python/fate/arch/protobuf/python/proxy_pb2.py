# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proxy.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import basic_meta_pb2 as basic__meta__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x0bproxy.proto\x12*com.webank.ai.eggroll.api.networking.proxy\x1a\x10\x62\x61sic-meta.proto"&\n\x05Model\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x64\x61taKey\x18\x02 \x01(\t"X\n\x04Task\x12\x0e\n\x06taskId\x18\x01 \x01(\t\x12@\n\x05model\x18\x02 \x01(\x0b\x32\x31.com.webank.ai.eggroll.api.networking.proxy.Model"p\n\x05Topic\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07partyId\x18\x02 \x01(\t\x12\x0c\n\x04role\x18\x03 \x01(\t\x12:\n\x08\x63\x61llback\x18\x04 \x01(\x0b\x32(.com.webank.ai.eggroll.api.core.Endpoint"\x17\n\x07\x43ommand\x12\x0c\n\x04name\x18\x01 \x01(\t"p\n\x04\x43onf\x12\x16\n\x0eoverallTimeout\x18\x01 \x01(\x03\x12\x1d\n\x15\x63ompletionWaitTimeout\x18\x02 \x01(\x03\x12\x1d\n\x15packetIntervalTimeout\x18\x03 \x01(\x03\x12\x12\n\nmaxRetries\x18\x04 \x01(\x05"\x9a\x03\n\x08Metadata\x12>\n\x04task\x18\x01 \x01(\x0b\x32\x30.com.webank.ai.eggroll.api.networking.proxy.Task\x12>\n\x03src\x18\x02 \x01(\x0b\x32\x31.com.webank.ai.eggroll.api.networking.proxy.Topic\x12>\n\x03\x64st\x18\x03 \x01(\x0b\x32\x31.com.webank.ai.eggroll.api.networking.proxy.Topic\x12\x44\n\x07\x63ommand\x18\x04 \x01(\x0b\x32\x33.com.webank.ai.eggroll.api.networking.proxy.Command\x12\x10\n\x08operator\x18\x05 \x01(\t\x12\x0b\n\x03seq\x18\x06 \x01(\x03\x12\x0b\n\x03\x61\x63k\x18\x07 \x01(\x03\x12>\n\x04\x63onf\x18\x08 \x01(\x0b\x32\x30.com.webank.ai.eggroll.api.networking.proxy.Conf\x12\x0b\n\x03\x65xt\x18\t \x01(\x0c\x12\x0f\n\x07version\x18\x64 \x01(\t""\n\x04\x44\x61ta\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c"\x8e\x01\n\x06Packet\x12\x44\n\x06header\x18\x01 \x01(\x0b\x32\x34.com.webank.ai.eggroll.api.networking.proxy.Metadata\x12>\n\x04\x62ody\x18\x02 \x01(\x0b\x32\x30.com.webank.ai.eggroll.api.networking.proxy.Data"\xa3\x01\n\x11HeartbeatResponse\x12\x44\n\x06header\x18\x01 \x01(\x0b\x32\x34.com.webank.ai.eggroll.api.networking.proxy.Metadata\x12H\n\toperation\x18\x02 \x01(\x0e\x32\x35.com.webank.ai.eggroll.api.networking.proxy.Operation"\xc5\x01\n\x0cPollingFrame\x12\x0e\n\x06method\x18\x01 \x01(\t\x12\x0b\n\x03seq\x18\x02 \x01(\x03\x12\x46\n\x08metadata\x18\n \x01(\x0b\x32\x34.com.webank.ai.eggroll.api.networking.proxy.Metadata\x12\x42\n\x06packet\x18\x14 \x01(\x0b\x32\x32.com.webank.ai.eggroll.api.networking.proxy.Packet\x12\x0c\n\x04\x64\x65sc\x18\x1e \x01(\t*O\n\tOperation\x12\t\n\x05START\x10\x00\x12\x07\n\x03RUN\x10\x01\x12\x08\n\x04STOP\x10\x02\x12\x08\n\x04KILL\x10\x03\x12\x0c\n\x08GET_DATA\x10\x04\x12\x0c\n\x08PUT_DATA\x10\x05\x32\xf6\x03\n\x13\x44\x61taTransferService\x12r\n\x04push\x12\x32.com.webank.ai.eggroll.api.networking.proxy.Packet\x1a\x34.com.webank.ai.eggroll.api.networking.proxy.Metadata(\x01\x12r\n\x04pull\x12\x34.com.webank.ai.eggroll.api.networking.proxy.Metadata\x1a\x32.com.webank.ai.eggroll.api.networking.proxy.Packet0\x01\x12s\n\tunaryCall\x12\x32.com.webank.ai.eggroll.api.networking.proxy.Packet\x1a\x32.com.webank.ai.eggroll.api.networking.proxy.Packet\x12\x81\x01\n\x07polling\x12\x38.com.webank.ai.eggroll.api.networking.proxy.PollingFrame\x1a\x38.com.webank.ai.eggroll.api.networking.proxy.PollingFrame(\x01\x30\x01\x32t\n\x0cRouteService\x12\x64\n\x05query\x12\x31.com.webank.ai.eggroll.api.networking.proxy.Topic\x1a(.com.webank.ai.eggroll.api.core.Endpointb\x06proto3'
)

_OPERATION = DESCRIPTOR.enum_types_by_name["Operation"]
Operation = enum_type_wrapper.EnumTypeWrapper(_OPERATION)
START = 0
RUN = 1
STOP = 2
KILL = 3
GET_DATA = 4
PUT_DATA = 5


_MODEL = DESCRIPTOR.message_types_by_name["Model"]
_TASK = DESCRIPTOR.message_types_by_name["Task"]
_TOPIC = DESCRIPTOR.message_types_by_name["Topic"]
_COMMAND = DESCRIPTOR.message_types_by_name["Command"]
_CONF = DESCRIPTOR.message_types_by_name["Conf"]
_METADATA = DESCRIPTOR.message_types_by_name["Metadata"]
_DATA = DESCRIPTOR.message_types_by_name["Data"]
_PACKET = DESCRIPTOR.message_types_by_name["Packet"]
_HEARTBEATRESPONSE = DESCRIPTOR.message_types_by_name["HeartbeatResponse"]
_POLLINGFRAME = DESCRIPTOR.message_types_by_name["PollingFrame"]
Model = _reflection.GeneratedProtocolMessageType(
    "Model",
    (_message.Message,),
    {
        "DESCRIPTOR": _MODEL,
        "__module__": "proxy_pb2"
        # @@protoc_insertion_point(class_scope:com.webank.ai.eggroll.api.networking.proxy.Model)
    },
)
_sym_db.RegisterMessage(Model)

Task = _reflection.GeneratedProtocolMessageType(
    "Task",
    (_message.Message,),
    {
        "DESCRIPTOR": _TASK,
        "__module__": "proxy_pb2"
        # @@protoc_insertion_point(class_scope:com.webank.ai.eggroll.api.networking.proxy.Task)
    },
)
_sym_db.RegisterMessage(Task)

Topic = _reflection.GeneratedProtocolMessageType(
    "Topic",
    (_message.Message,),
    {
        "DESCRIPTOR": _TOPIC,
        "__module__": "proxy_pb2"
        # @@protoc_insertion_point(class_scope:com.webank.ai.eggroll.api.networking.proxy.Topic)
    },
)
_sym_db.RegisterMessage(Topic)

Command = _reflection.GeneratedProtocolMessageType(
    "Command",
    (_message.Message,),
    {
        "DESCRIPTOR": _COMMAND,
        "__module__": "proxy_pb2"
        # @@protoc_insertion_point(class_scope:com.webank.ai.eggroll.api.networking.proxy.Command)
    },
)
_sym_db.RegisterMessage(Command)

Conf = _reflection.GeneratedProtocolMessageType(
    "Conf",
    (_message.Message,),
    {
        "DESCRIPTOR": _CONF,
        "__module__": "proxy_pb2"
        # @@protoc_insertion_point(class_scope:com.webank.ai.eggroll.api.networking.proxy.Conf)
    },
)
_sym_db.RegisterMessage(Conf)

Metadata = _reflection.GeneratedProtocolMessageType(
    "Metadata",
    (_message.Message,),
    {
        "DESCRIPTOR": _METADATA,
        "__module__": "proxy_pb2"
        # @@protoc_insertion_point(class_scope:com.webank.ai.eggroll.api.networking.proxy.Metadata)
    },
)
_sym_db.RegisterMessage(Metadata)

Data = _reflection.GeneratedProtocolMessageType(
    "Data",
    (_message.Message,),
    {
        "DESCRIPTOR": _DATA,
        "__module__": "proxy_pb2"
        # @@protoc_insertion_point(class_scope:com.webank.ai.eggroll.api.networking.proxy.Data)
    },
)
_sym_db.RegisterMessage(Data)

Packet = _reflection.GeneratedProtocolMessageType(
    "Packet",
    (_message.Message,),
    {
        "DESCRIPTOR": _PACKET,
        "__module__": "proxy_pb2"
        # @@protoc_insertion_point(class_scope:com.webank.ai.eggroll.api.networking.proxy.Packet)
    },
)
_sym_db.RegisterMessage(Packet)

HeartbeatResponse = _reflection.GeneratedProtocolMessageType(
    "HeartbeatResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _HEARTBEATRESPONSE,
        "__module__": "proxy_pb2"
        # @@protoc_insertion_point(class_scope:com.webank.ai.eggroll.api.networking.proxy.HeartbeatResponse)
    },
)
_sym_db.RegisterMessage(HeartbeatResponse)

PollingFrame = _reflection.GeneratedProtocolMessageType(
    "PollingFrame",
    (_message.Message,),
    {
        "DESCRIPTOR": _POLLINGFRAME,
        "__module__": "proxy_pb2"
        # @@protoc_insertion_point(class_scope:com.webank.ai.eggroll.api.networking.proxy.PollingFrame)
    },
)
_sym_db.RegisterMessage(PollingFrame)

_DATATRANSFERSERVICE = DESCRIPTOR.services_by_name["DataTransferService"]
_ROUTESERVICE = DESCRIPTOR.services_by_name["RouteService"]
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _OPERATION._serialized_start = 1420
    _OPERATION._serialized_end = 1499
    _MODEL._serialized_start = 77
    _MODEL._serialized_end = 115
    _TASK._serialized_start = 117
    _TASK._serialized_end = 205
    _TOPIC._serialized_start = 207
    _TOPIC._serialized_end = 319
    _COMMAND._serialized_start = 321
    _COMMAND._serialized_end = 344
    _CONF._serialized_start = 346
    _CONF._serialized_end = 458
    _METADATA._serialized_start = 461
    _METADATA._serialized_end = 871
    _DATA._serialized_start = 873
    _DATA._serialized_end = 907
    _PACKET._serialized_start = 910
    _PACKET._serialized_end = 1052
    _HEARTBEATRESPONSE._serialized_start = 1055
    _HEARTBEATRESPONSE._serialized_end = 1218
    _POLLINGFRAME._serialized_start = 1221
    _POLLINGFRAME._serialized_end = 1418
    _DATATRANSFERSERVICE._serialized_start = 1502
    _DATATRANSFERSERVICE._serialized_end = 2004
    _ROUTESERVICE._serialized_start = 2006
    _ROUTESERVICE._serialized_end = 2122
# @@protoc_insertion_point(module_scope)
