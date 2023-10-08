# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import osx_pb2 as osx__pb2


class PrivateTransferProtocolStub(object):
    """互联互通如果使用异步传输协议作为标准参考，Header会复用metadata传输互联互通协议报头，且metadata中会传输异步场景下的消息相关属性
    互联互通如果使用其他协议作为参考标准，Header会复用metadata传输互联互通协议报头
    互联互通如果使用GRPC作为参考标准，Header会复用HTTP2的报头传输互联互通协议报头

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.transport = channel.stream_stream(
                '/org.ppc.ptp.PrivateTransferProtocol/transport',
                request_serializer=osx__pb2.Inbound.SerializeToString,
                response_deserializer=osx__pb2.Outbound.FromString,
                )
        self.invoke = channel.unary_unary(
                '/org.ppc.ptp.PrivateTransferProtocol/invoke',
                request_serializer=osx__pb2.Inbound.SerializeToString,
                response_deserializer=osx__pb2.Outbound.FromString,
                )
        self.clusterTokenApply = channel.stream_stream(
                '/org.ppc.ptp.PrivateTransferProtocol/clusterTokenApply',
                request_serializer=osx__pb2.Inbound.SerializeToString,
                response_deserializer=osx__pb2.Outbound.FromString,
                )
        self.clusterTopicApply = channel.stream_stream(
                '/org.ppc.ptp.PrivateTransferProtocol/clusterTopicApply',
                request_serializer=osx__pb2.Inbound.SerializeToString,
                response_deserializer=osx__pb2.Outbound.FromString,
                )
        self.peek = channel.unary_unary(
                '/org.ppc.ptp.PrivateTransferProtocol/peek',
                request_serializer=osx__pb2.PeekInbound.SerializeToString,
                response_deserializer=osx__pb2.TransportOutbound.FromString,
                )
        self.pop = channel.unary_unary(
                '/org.ppc.ptp.PrivateTransferProtocol/pop',
                request_serializer=osx__pb2.PopInbound.SerializeToString,
                response_deserializer=osx__pb2.TransportOutbound.FromString,
                )
        self.push = channel.unary_unary(
                '/org.ppc.ptp.PrivateTransferProtocol/push',
                request_serializer=osx__pb2.PushInbound.SerializeToString,
                response_deserializer=osx__pb2.TransportOutbound.FromString,
                )
        self.release = channel.unary_unary(
                '/org.ppc.ptp.PrivateTransferProtocol/release',
                request_serializer=osx__pb2.ReleaseInbound.SerializeToString,
                response_deserializer=osx__pb2.TransportOutbound.FromString,
                )


class PrivateTransferProtocolServicer(object):
    """互联互通如果使用异步传输协议作为标准参考，Header会复用metadata传输互联互通协议报头，且metadata中会传输异步场景下的消息相关属性
    互联互通如果使用其他协议作为参考标准，Header会复用metadata传输互联互通协议报头
    互联互通如果使用GRPC作为参考标准，Header会复用HTTP2的报头传输互联互通协议报头

    """

    def transport(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def invoke(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def clusterTokenApply(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def clusterTopicApply(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def peek(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def pop(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def push(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def release(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PrivateTransferProtocolServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'transport': grpc.stream_stream_rpc_method_handler(
                    servicer.transport,
                    request_deserializer=osx__pb2.Inbound.FromString,
                    response_serializer=osx__pb2.Outbound.SerializeToString,
            ),
            'invoke': grpc.unary_unary_rpc_method_handler(
                    servicer.invoke,
                    request_deserializer=osx__pb2.Inbound.FromString,
                    response_serializer=osx__pb2.Outbound.SerializeToString,
            ),
            'clusterTokenApply': grpc.stream_stream_rpc_method_handler(
                    servicer.clusterTokenApply,
                    request_deserializer=osx__pb2.Inbound.FromString,
                    response_serializer=osx__pb2.Outbound.SerializeToString,
            ),
            'clusterTopicApply': grpc.stream_stream_rpc_method_handler(
                    servicer.clusterTopicApply,
                    request_deserializer=osx__pb2.Inbound.FromString,
                    response_serializer=osx__pb2.Outbound.SerializeToString,
            ),
            'peek': grpc.unary_unary_rpc_method_handler(
                    servicer.peek,
                    request_deserializer=osx__pb2.PeekInbound.FromString,
                    response_serializer=osx__pb2.TransportOutbound.SerializeToString,
            ),
            'pop': grpc.unary_unary_rpc_method_handler(
                    servicer.pop,
                    request_deserializer=osx__pb2.PopInbound.FromString,
                    response_serializer=osx__pb2.TransportOutbound.SerializeToString,
            ),
            'push': grpc.unary_unary_rpc_method_handler(
                    servicer.push,
                    request_deserializer=osx__pb2.PushInbound.FromString,
                    response_serializer=osx__pb2.TransportOutbound.SerializeToString,
            ),
            'release': grpc.unary_unary_rpc_method_handler(
                    servicer.release,
                    request_deserializer=osx__pb2.ReleaseInbound.FromString,
                    response_serializer=osx__pb2.TransportOutbound.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'org.ppc.ptp.PrivateTransferProtocol', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PrivateTransferProtocol(object):
    """互联互通如果使用异步传输协议作为标准参考，Header会复用metadata传输互联互通协议报头，且metadata中会传输异步场景下的消息相关属性
    互联互通如果使用其他协议作为参考标准，Header会复用metadata传输互联互通协议报头
    互联互通如果使用GRPC作为参考标准，Header会复用HTTP2的报头传输互联互通协议报头

    """

    @staticmethod
    def transport(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/org.ppc.ptp.PrivateTransferProtocol/transport',
            osx__pb2.Inbound.SerializeToString,
            osx__pb2.Outbound.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def invoke(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.ppc.ptp.PrivateTransferProtocol/invoke',
            osx__pb2.Inbound.SerializeToString,
            osx__pb2.Outbound.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def clusterTokenApply(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/org.ppc.ptp.PrivateTransferProtocol/clusterTokenApply',
            osx__pb2.Inbound.SerializeToString,
            osx__pb2.Outbound.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def clusterTopicApply(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/org.ppc.ptp.PrivateTransferProtocol/clusterTopicApply',
            osx__pb2.Inbound.SerializeToString,
            osx__pb2.Outbound.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def peek(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.ppc.ptp.PrivateTransferProtocol/peek',
            osx__pb2.PeekInbound.SerializeToString,
            osx__pb2.TransportOutbound.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def pop(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.ppc.ptp.PrivateTransferProtocol/pop',
            osx__pb2.PopInbound.SerializeToString,
            osx__pb2.TransportOutbound.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def push(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.ppc.ptp.PrivateTransferProtocol/push',
            osx__pb2.PushInbound.SerializeToString,
            osx__pb2.TransportOutbound.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def release(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.ppc.ptp.PrivateTransferProtocol/release',
            osx__pb2.ReleaseInbound.SerializeToString,
            osx__pb2.TransportOutbound.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
