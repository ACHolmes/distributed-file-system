# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import chat_pb2 as chat__pb2


class ClientHandlerStub(object):
    """The ClientHandler service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListUsers = channel.unary_unary(
                '/ClientHandler/ListUsers',
                request_serializer=chat__pb2.ListRequest.SerializeToString,
                response_deserializer=chat__pb2.ListReply.FromString,
                )
        self.Login = channel.unary_unary(
                '/ClientHandler/Login',
                request_serializer=chat__pb2.LoginRequest.SerializeToString,
                response_deserializer=chat__pb2.LoginReply.FromString,
                )
        self.Logout = channel.unary_unary(
                '/ClientHandler/Logout',
                request_serializer=chat__pb2.LogoutRequest.SerializeToString,
                response_deserializer=chat__pb2.LogoutReply.FromString,
                )
        self.Send = channel.unary_unary(
                '/ClientHandler/Send',
                request_serializer=chat__pb2.SendRequest.SerializeToString,
                response_deserializer=chat__pb2.SendReply.FromString,
                )
        self.GetMessages = channel.unary_unary(
                '/ClientHandler/GetMessages',
                request_serializer=chat__pb2.GetRequest.SerializeToString,
                response_deserializer=chat__pb2.GetReply.FromString,
                )
        self.Delete = channel.unary_unary(
                '/ClientHandler/Delete',
                request_serializer=chat__pb2.DeleteRequest.SerializeToString,
                response_deserializer=chat__pb2.DeleteReply.FromString,
                )
        self.GetBackups = channel.unary_unary(
                '/ClientHandler/GetBackups',
                request_serializer=chat__pb2.BackupRequest.SerializeToString,
                response_deserializer=chat__pb2.BackupReply.FromString,
                )
        self.AddUser = channel.unary_unary(
                '/ClientHandler/AddUser',
                request_serializer=chat__pb2.LoginRequest.SerializeToString,
                response_deserializer=chat__pb2.Empty.FromString,
                )
        self.RemoveUser = channel.unary_unary(
                '/ClientHandler/RemoveUser',
                request_serializer=chat__pb2.DeleteRequest.SerializeToString,
                response_deserializer=chat__pb2.Empty.FromString,
                )
        self.SetUserStatus = channel.unary_unary(
                '/ClientHandler/SetUserStatus',
                request_serializer=chat__pb2.SetStatusRequest.SerializeToString,
                response_deserializer=chat__pb2.Empty.FromString,
                )
        self.AddMessage = channel.unary_unary(
                '/ClientHandler/AddMessage',
                request_serializer=chat__pb2.SendRequest.SerializeToString,
                response_deserializer=chat__pb2.Empty.FromString,
                )
        self.DeleteMessages = channel.unary_unary(
                '/ClientHandler/DeleteMessages',
                request_serializer=chat__pb2.GetRequest.SerializeToString,
                response_deserializer=chat__pb2.Empty.FromString,
                )
        self.PullData = channel.unary_unary(
                '/ClientHandler/PullData',
                request_serializer=chat__pb2.Empty.SerializeToString,
                response_deserializer=chat__pb2.Data.FromString,
                )
        self.CheckClock = channel.unary_unary(
                '/ClientHandler/CheckClock',
                request_serializer=chat__pb2.Empty.SerializeToString,
                response_deserializer=chat__pb2.Clock.FromString,
                )


class ClientHandlerServicer(object):
    """The ClientHandler service definition.
    """

    def ListUsers(self, request, context):
        """Lists users
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Login(self, request, context):
        """Requests to Login
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Logout(self, request, context):
        """Requests to Logout
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Send(self, request, context):
        """Attempts to Send message
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMessages(self, request, context):
        """Attempts to receive new messages
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Attempts to delete account
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBackups(self, request, context):
        """Creates backup chain
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddUser(self, request, context):
        """Methods to be used by ServerWorkers
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetUserStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteMessages(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PullData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckClock(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ClientHandlerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListUsers': grpc.unary_unary_rpc_method_handler(
                    servicer.ListUsers,
                    request_deserializer=chat__pb2.ListRequest.FromString,
                    response_serializer=chat__pb2.ListReply.SerializeToString,
            ),
            'Login': grpc.unary_unary_rpc_method_handler(
                    servicer.Login,
                    request_deserializer=chat__pb2.LoginRequest.FromString,
                    response_serializer=chat__pb2.LoginReply.SerializeToString,
            ),
            'Logout': grpc.unary_unary_rpc_method_handler(
                    servicer.Logout,
                    request_deserializer=chat__pb2.LogoutRequest.FromString,
                    response_serializer=chat__pb2.LogoutReply.SerializeToString,
            ),
            'Send': grpc.unary_unary_rpc_method_handler(
                    servicer.Send,
                    request_deserializer=chat__pb2.SendRequest.FromString,
                    response_serializer=chat__pb2.SendReply.SerializeToString,
            ),
            'GetMessages': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMessages,
                    request_deserializer=chat__pb2.GetRequest.FromString,
                    response_serializer=chat__pb2.GetReply.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=chat__pb2.DeleteRequest.FromString,
                    response_serializer=chat__pb2.DeleteReply.SerializeToString,
            ),
            'GetBackups': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBackups,
                    request_deserializer=chat__pb2.BackupRequest.FromString,
                    response_serializer=chat__pb2.BackupReply.SerializeToString,
            ),
            'AddUser': grpc.unary_unary_rpc_method_handler(
                    servicer.AddUser,
                    request_deserializer=chat__pb2.LoginRequest.FromString,
                    response_serializer=chat__pb2.Empty.SerializeToString,
            ),
            'RemoveUser': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveUser,
                    request_deserializer=chat__pb2.DeleteRequest.FromString,
                    response_serializer=chat__pb2.Empty.SerializeToString,
            ),
            'SetUserStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.SetUserStatus,
                    request_deserializer=chat__pb2.SetStatusRequest.FromString,
                    response_serializer=chat__pb2.Empty.SerializeToString,
            ),
            'AddMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.AddMessage,
                    request_deserializer=chat__pb2.SendRequest.FromString,
                    response_serializer=chat__pb2.Empty.SerializeToString,
            ),
            'DeleteMessages': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteMessages,
                    request_deserializer=chat__pb2.GetRequest.FromString,
                    response_serializer=chat__pb2.Empty.SerializeToString,
            ),
            'PullData': grpc.unary_unary_rpc_method_handler(
                    servicer.PullData,
                    request_deserializer=chat__pb2.Empty.FromString,
                    response_serializer=chat__pb2.Data.SerializeToString,
            ),
            'CheckClock': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckClock,
                    request_deserializer=chat__pb2.Empty.FromString,
                    response_serializer=chat__pb2.Clock.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ClientHandler', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ClientHandler(object):
    """The ClientHandler service definition.
    """

    @staticmethod
    def ListUsers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ClientHandler/ListUsers',
            chat__pb2.ListRequest.SerializeToString,
            chat__pb2.ListReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Login(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ClientHandler/Login',
            chat__pb2.LoginRequest.SerializeToString,
            chat__pb2.LoginReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Logout(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ClientHandler/Logout',
            chat__pb2.LogoutRequest.SerializeToString,
            chat__pb2.LogoutReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Send(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ClientHandler/Send',
            chat__pb2.SendRequest.SerializeToString,
            chat__pb2.SendReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMessages(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ClientHandler/GetMessages',
            chat__pb2.GetRequest.SerializeToString,
            chat__pb2.GetReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ClientHandler/Delete',
            chat__pb2.DeleteRequest.SerializeToString,
            chat__pb2.DeleteReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBackups(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ClientHandler/GetBackups',
            chat__pb2.BackupRequest.SerializeToString,
            chat__pb2.BackupReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ClientHandler/AddUser',
            chat__pb2.LoginRequest.SerializeToString,
            chat__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ClientHandler/RemoveUser',
            chat__pb2.DeleteRequest.SerializeToString,
            chat__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetUserStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ClientHandler/SetUserStatus',
            chat__pb2.SetStatusRequest.SerializeToString,
            chat__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ClientHandler/AddMessage',
            chat__pb2.SendRequest.SerializeToString,
            chat__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteMessages(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ClientHandler/DeleteMessages',
            chat__pb2.GetRequest.SerializeToString,
            chat__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PullData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ClientHandler/PullData',
            chat__pb2.Empty.SerializeToString,
            chat__pb2.Data.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckClock(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ClientHandler/CheckClock',
            chat__pb2.Empty.SerializeToString,
            chat__pb2.Clock.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
