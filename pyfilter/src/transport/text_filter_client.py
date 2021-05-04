from typing import Tuple, Text, Iterator, Iterable, NoReturn, Callable

import grpc
from grpc import Channel

from transport.proto import (
    TextFilterServiceStub,
    SingleTextFilterRequest,
)


class TextFilterClient:

    def __init__(self, svc_channel: Channel, svc_client_stub: TextFilterServiceStub, quiet: bool):
        """
        The client wrapper for the TextFilter.

        :param svc_channel: The channel used to instantiate the stub. Only used for debugging and graceful exiting
        :param svc_client_stub: The backend being wrapped.
        :param quiet: If True, will suppress debug output
        """
        self._channel: Channel = svc_channel
        self._client: TextFilterServiceStub = svc_client_stub
        self.quiet = quiet  # TODO: Add logger and pass this to it instead

    @property
    def client(self) -> TextFilterServiceStub:
        return self._client

    @classmethod
    def new(cls, secure_port, insecure_port, quiet) -> 'TextFilterClient':
        """
        Alternate constructor using just a port

        :param secure_port: [UNIMPLEMENTED] A secure port to use for hosting the server (default option if specified)
        :param insecure_port: An insecure port to use for hosting the server (only used if secure port is None)
        :param quiet: If True, will suppress debug output
        :return: A more functional wrapper for the Client stub
        """
        channel, stub = cls._get_client_stub(secure_port, insecure_port)
        return TextFilterClient(channel, stub, quiet)

    @classmethod
    def _get_client_stub(cls, secure_port: int = None, insecure_port: int = None) -> Tuple[Channel,
                                                                                           TextFilterServiceStub]:
        """
        Constructs a Filter Client Stub via a channel

        :param secure_port: [UNIMPLEMENTED] A secure port to connect to the server on (default option if specified)
        :param insecure_port: An insecure port to connect to the server on (only used if secure port is None)
        :return: The gRPC Client Stub
        """

        channel = cls._get_channel(secure=secure_port is not None, port=secure_port or insecure_port)
        return channel, TextFilterServiceStub(channel)

    @staticmethod
    def _get_channel(secure: bool, port: int) -> Channel:
        """
        Creates a gRPC channel via which to communicate with the server
        :param secure: [UNIMPLEMENTED] Is this a secured (SSL) channel?
        :param port: What port to connect on
        :return: A gRPC channel
        """
        if secure:
            return grpc.secure_channel(f'localhost:{port}', credentials='NOT IMPLEMENTED')
        else:
            return grpc.insecure_channel(f'localhost:{port}')

    def filter(self, input_string: Text, casefold: bool) -> bool:
        """
        This is the client implementation of the TextFilter's filter method. For more info, see there.
        """
        if not self.quiet:
            print(f'Sending filter request: input="{input_string}", casefold:{casefold}')
        request = SingleTextFilterRequest(input_string=input_string, casefold=casefold)
        response = self.client.SingleFilter(request)
        return response.passed_filter

    def multi_filter(self, input_strings: Iterable[Text], casefold: bool) -> Iterable[Text]:
        """
        This is the client implementation of the TextFilter's multi_filter method. For more info, see there.
        """
        if not self.quiet:
            print(f'Sending multi filter request: input="{input_strings}", casefold:{casefold}')
        request = (SingleTextFilterRequest(input_string=input_, casefold=casefold) for input_ in input_strings)
        response = self.client.MultiFilter(request)
        return response.passed_inputs

    def multi_filter_stream(self, input_strings: Iterable[Text], casefold: bool) -> Iterator[bool]:
        """
        This is a custom bi-directional filter streaming API which takes an iterator of inputs and yields each output.
        """
        if not self.quiet:
            print(f'Sending multi filter stream request: input="{input_strings}", casefold:{casefold}')
        request = (SingleTextFilterRequest(input_string=input_, casefold=casefold) for input_ in input_strings)
        for response in self.client.MultiFilterStream(request):
            yield response.passed_filter

    def subscribe(self, callback: Callable) -> NoReturn:
        """
        Debug only: Subscribe to the channel state changes and handle via a callback
        """
        self._channel.subscribe(callback, try_to_connect=True)

    def unsubscribe(self, callback: Callable) -> NoReturn:
        """
        Debug only: Unsubscribe from the channel state changes and handle via a callback
        """
        self._channel.unsubscribe(callback)

    def quit(self) -> NoReturn:
        """
        Close the channel
        """
        self._channel.close()

    def __del__(self):
        # Don't leave the channel up!
        self.quit()
