# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import pubsub_pb2 as src_dot_ray_dot_protobuf_dot_pubsub__pb2


class SubscriberServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PubsubLongPolling = channel.unary_unary(
                '/ray.rpc.SubscriberService/PubsubLongPolling',
                request_serializer=src_dot_ray_dot_protobuf_dot_pubsub__pb2.PubsubLongPollingRequest.SerializeToString,
                response_deserializer=src_dot_ray_dot_protobuf_dot_pubsub__pb2.PubsubLongPollingReply.FromString,
                )
        self.PubsubCommandBatch = channel.unary_unary(
                '/ray.rpc.SubscriberService/PubsubCommandBatch',
                request_serializer=src_dot_ray_dot_protobuf_dot_pubsub__pb2.PubsubCommandBatchRequest.SerializeToString,
                response_deserializer=src_dot_ray_dot_protobuf_dot_pubsub__pb2.PubsubCommandBatchReply.FromString,
                )


class SubscriberServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def PubsubLongPolling(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PubsubCommandBatch(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SubscriberServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'PubsubLongPolling': grpc.unary_unary_rpc_method_handler(
                    servicer.PubsubLongPolling,
                    request_deserializer=src_dot_ray_dot_protobuf_dot_pubsub__pb2.PubsubLongPollingRequest.FromString,
                    response_serializer=src_dot_ray_dot_protobuf_dot_pubsub__pb2.PubsubLongPollingReply.SerializeToString,
            ),
            'PubsubCommandBatch': grpc.unary_unary_rpc_method_handler(
                    servicer.PubsubCommandBatch,
                    request_deserializer=src_dot_ray_dot_protobuf_dot_pubsub__pb2.PubsubCommandBatchRequest.FromString,
                    response_serializer=src_dot_ray_dot_protobuf_dot_pubsub__pb2.PubsubCommandBatchReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ray.rpc.SubscriberService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SubscriberService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def PubsubLongPolling(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ray.rpc.SubscriberService/PubsubLongPolling',
            src_dot_ray_dot_protobuf_dot_pubsub__pb2.PubsubLongPollingRequest.SerializeToString,
            src_dot_ray_dot_protobuf_dot_pubsub__pb2.PubsubLongPollingReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PubsubCommandBatch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ray.rpc.SubscriberService/PubsubCommandBatch',
            src_dot_ray_dot_protobuf_dot_pubsub__pb2.PubsubCommandBatchRequest.SerializeToString,
            src_dot_ray_dot_protobuf_dot_pubsub__pb2.PubsubCommandBatchReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
