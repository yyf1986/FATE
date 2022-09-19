# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: basic-meta.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x10\x62\x61sic-meta.proto\x12\x1e\x63om.webank.ai.eggroll.api.core"6\n\x08\x45ndpoint\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\x12\x10\n\x08hostname\x18\x03 \x01(\t"H\n\tEndpoints\x12;\n\tendpoints\x18\x01 \x03(\x0b\x32(.com.webank.ai.eggroll.api.core.Endpoint"H\n\x04\x44\x61ta\x12\x0e\n\x06isNull\x18\x01 \x01(\x08\x12\x14\n\x0chostLanguage\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\x0c"F\n\x0cRepeatedData\x12\x36\n\x08\x64\x61talist\x18\x01 \x03(\x0b\x32$.com.webank.ai.eggroll.api.core.Data"u\n\x0b\x43\x61llRequest\x12\x0f\n\x07isAsync\x18\x01 \x01(\x08\x12\x0f\n\x07timeout\x18\x02 \x01(\x03\x12\x0f\n\x07\x63ommand\x18\x03 \x01(\t\x12\x33\n\x05param\x18\x04 \x01(\x0b\x32$.com.webank.ai.eggroll.api.core.Data"\x88\x01\n\x0c\x43\x61llResponse\x12\x42\n\x0creturnStatus\x18\x01 \x01(\x0b\x32,.com.webank.ai.eggroll.api.core.ReturnStatus\x12\x34\n\x06result\x18\x02 \x01(\x0b\x32$.com.webank.ai.eggroll.api.core.Data""\n\x03Job\x12\r\n\x05jobId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t"Y\n\x04Task\x12\x30\n\x03job\x18\x01 \x01(\x0b\x32#.com.webank.ai.eggroll.api.core.Job\x12\x0e\n\x06taskId\x18\x02 \x01(\x03\x12\x0f\n\x07tableId\x18\x03 \x01(\x03"N\n\x06Result\x12\x32\n\x04task\x18\x01 \x01(\x0b\x32$.com.webank.ai.eggroll.api.core.Task\x12\x10\n\x08resultId\x18\x02 \x01(\x03"-\n\x0cReturnStatus\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t"\xe2\x01\n\x0bSessionInfo\x12\x11\n\tsessionId\x18\x01 \x01(\t\x12\x61\n\x13\x63omputingEngineConf\x18\x02 \x03(\x0b\x32\x44.com.webank.ai.eggroll.api.core.SessionInfo.ComputingEngineConfEntry\x12\x14\n\x0cnamingPolicy\x18\x03 \x01(\t\x12\x0b\n\x03tag\x18\x04 \x01(\t\x1a:\n\x18\x43omputingEngineConfEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x62\x06proto3'
)


_ENDPOINT = DESCRIPTOR.message_types_by_name["Endpoint"]
_ENDPOINTS = DESCRIPTOR.message_types_by_name["Endpoints"]
_DATA = DESCRIPTOR.message_types_by_name["Data"]
_REPEATEDDATA = DESCRIPTOR.message_types_by_name["RepeatedData"]
_CALLREQUEST = DESCRIPTOR.message_types_by_name["CallRequest"]
_CALLRESPONSE = DESCRIPTOR.message_types_by_name["CallResponse"]
_JOB = DESCRIPTOR.message_types_by_name["Job"]
_TASK = DESCRIPTOR.message_types_by_name["Task"]
_RESULT = DESCRIPTOR.message_types_by_name["Result"]
_RETURNSTATUS = DESCRIPTOR.message_types_by_name["ReturnStatus"]
_SESSIONINFO = DESCRIPTOR.message_types_by_name["SessionInfo"]
_SESSIONINFO_COMPUTINGENGINECONFENTRY = _SESSIONINFO.nested_types_by_name[
    "ComputingEngineConfEntry"
]
Endpoint = _reflection.GeneratedProtocolMessageType(
    "Endpoint",
    (_message.Message,),
    {
        "DESCRIPTOR": _ENDPOINT,
        "__module__": "basic_meta_pb2"
        # @@protoc_insertion_point(class_scope:com.webank.ai.eggroll.api.core.Endpoint)
    },
)
_sym_db.RegisterMessage(Endpoint)

Endpoints = _reflection.GeneratedProtocolMessageType(
    "Endpoints",
    (_message.Message,),
    {
        "DESCRIPTOR": _ENDPOINTS,
        "__module__": "basic_meta_pb2"
        # @@protoc_insertion_point(class_scope:com.webank.ai.eggroll.api.core.Endpoints)
    },
)
_sym_db.RegisterMessage(Endpoints)

Data = _reflection.GeneratedProtocolMessageType(
    "Data",
    (_message.Message,),
    {
        "DESCRIPTOR": _DATA,
        "__module__": "basic_meta_pb2"
        # @@protoc_insertion_point(class_scope:com.webank.ai.eggroll.api.core.Data)
    },
)
_sym_db.RegisterMessage(Data)

RepeatedData = _reflection.GeneratedProtocolMessageType(
    "RepeatedData",
    (_message.Message,),
    {
        "DESCRIPTOR": _REPEATEDDATA,
        "__module__": "basic_meta_pb2"
        # @@protoc_insertion_point(class_scope:com.webank.ai.eggroll.api.core.RepeatedData)
    },
)
_sym_db.RegisterMessage(RepeatedData)

CallRequest = _reflection.GeneratedProtocolMessageType(
    "CallRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _CALLREQUEST,
        "__module__": "basic_meta_pb2"
        # @@protoc_insertion_point(class_scope:com.webank.ai.eggroll.api.core.CallRequest)
    },
)
_sym_db.RegisterMessage(CallRequest)

CallResponse = _reflection.GeneratedProtocolMessageType(
    "CallResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _CALLRESPONSE,
        "__module__": "basic_meta_pb2"
        # @@protoc_insertion_point(class_scope:com.webank.ai.eggroll.api.core.CallResponse)
    },
)
_sym_db.RegisterMessage(CallResponse)

Job = _reflection.GeneratedProtocolMessageType(
    "Job",
    (_message.Message,),
    {
        "DESCRIPTOR": _JOB,
        "__module__": "basic_meta_pb2"
        # @@protoc_insertion_point(class_scope:com.webank.ai.eggroll.api.core.Job)
    },
)
_sym_db.RegisterMessage(Job)

Task = _reflection.GeneratedProtocolMessageType(
    "Task",
    (_message.Message,),
    {
        "DESCRIPTOR": _TASK,
        "__module__": "basic_meta_pb2"
        # @@protoc_insertion_point(class_scope:com.webank.ai.eggroll.api.core.Task)
    },
)
_sym_db.RegisterMessage(Task)

Result = _reflection.GeneratedProtocolMessageType(
    "Result",
    (_message.Message,),
    {
        "DESCRIPTOR": _RESULT,
        "__module__": "basic_meta_pb2"
        # @@protoc_insertion_point(class_scope:com.webank.ai.eggroll.api.core.Result)
    },
)
_sym_db.RegisterMessage(Result)

ReturnStatus = _reflection.GeneratedProtocolMessageType(
    "ReturnStatus",
    (_message.Message,),
    {
        "DESCRIPTOR": _RETURNSTATUS,
        "__module__": "basic_meta_pb2"
        # @@protoc_insertion_point(class_scope:com.webank.ai.eggroll.api.core.ReturnStatus)
    },
)
_sym_db.RegisterMessage(ReturnStatus)

SessionInfo = _reflection.GeneratedProtocolMessageType(
    "SessionInfo",
    (_message.Message,),
    {
        "ComputingEngineConfEntry": _reflection.GeneratedProtocolMessageType(
            "ComputingEngineConfEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _SESSIONINFO_COMPUTINGENGINECONFENTRY,
                "__module__": "basic_meta_pb2"
                # @@protoc_insertion_point(class_scope:com.webank.ai.eggroll.api.core.SessionInfo.ComputingEngineConfEntry)
            },
        ),
        "DESCRIPTOR": _SESSIONINFO,
        "__module__": "basic_meta_pb2"
        # @@protoc_insertion_point(class_scope:com.webank.ai.eggroll.api.core.SessionInfo)
    },
)
_sym_db.RegisterMessage(SessionInfo)
_sym_db.RegisterMessage(SessionInfo.ComputingEngineConfEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _SESSIONINFO_COMPUTINGENGINECONFENTRY._options = None
    _SESSIONINFO_COMPUTINGENGINECONFENTRY._serialized_options = b"8\001"
    _ENDPOINT._serialized_start = 52
    _ENDPOINT._serialized_end = 106
    _ENDPOINTS._serialized_start = 108
    _ENDPOINTS._serialized_end = 180
    _DATA._serialized_start = 182
    _DATA._serialized_end = 254
    _REPEATEDDATA._serialized_start = 256
    _REPEATEDDATA._serialized_end = 326
    _CALLREQUEST._serialized_start = 328
    _CALLREQUEST._serialized_end = 445
    _CALLRESPONSE._serialized_start = 448
    _CALLRESPONSE._serialized_end = 584
    _JOB._serialized_start = 586
    _JOB._serialized_end = 620
    _TASK._serialized_start = 622
    _TASK._serialized_end = 711
    _RESULT._serialized_start = 713
    _RESULT._serialized_end = 791
    _RETURNSTATUS._serialized_start = 793
    _RETURNSTATUS._serialized_end = 838
    _SESSIONINFO._serialized_start = 841
    _SESSIONINFO._serialized_end = 1067
    _SESSIONINFO_COMPUTINGENGINECONFENTRY._serialized_start = 1009
    _SESSIONINFO_COMPUTINGENGINECONFENTRY._serialized_end = 1067
# @@protoc_insertion_point(module_scope)
