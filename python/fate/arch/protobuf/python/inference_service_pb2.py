# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: inference_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x17inference_service.proto\x12\x1e\x63om.webank.ai.fate.api.serving"0\n\x10InferenceMessage\x12\x0e\n\x06header\x18\x01 \x01(\x0c\x12\x0c\n\x04\x62ody\x18\x02 \x01(\x0c\x32\xf6\x02\n\x10InferenceService\x12o\n\tinference\x12\x30.com.webank.ai.fate.api.serving.InferenceMessage\x1a\x30.com.webank.ai.fate.api.serving.InferenceMessage\x12w\n\x11startInferenceJob\x12\x30.com.webank.ai.fate.api.serving.InferenceMessage\x1a\x30.com.webank.ai.fate.api.serving.InferenceMessage\x12x\n\x12getInferenceResult\x12\x30.com.webank.ai.fate.api.serving.InferenceMessage\x1a\x30.com.webank.ai.fate.api.serving.InferenceMessageB\x17\x42\x15InferenceServiceProtob\x06proto3'
)


_INFERENCEMESSAGE = DESCRIPTOR.message_types_by_name["InferenceMessage"]
InferenceMessage = _reflection.GeneratedProtocolMessageType(
    "InferenceMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _INFERENCEMESSAGE,
        "__module__": "inference_service_pb2"
        # @@protoc_insertion_point(class_scope:com.webank.ai.fate.api.serving.InferenceMessage)
    },
)
_sym_db.RegisterMessage(InferenceMessage)

_INFERENCESERVICE = DESCRIPTOR.services_by_name["InferenceService"]
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"B\025InferenceServiceProto"
    _INFERENCEMESSAGE._serialized_start = 59
    _INFERENCEMESSAGE._serialized_end = 107
    _INFERENCESERVICE._serialized_start = 110
    _INFERENCESERVICE._serialized_end = 484
# @@protoc_insertion_point(module_scope)
