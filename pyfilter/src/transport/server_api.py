import threading
from concurrent.futures import ThreadPoolExecutor
import grpc
from transport.proto import add_TextFilterServiceServicer_to_server
from transport.text_filter_service import TextFilterService


def start_server_with_service(service: TextFilterService, secure_port: int = None,
                              insecure_port: int = None, max_workers: int = 10) -> grpc.Server:
    """
    A bootstrap API to start the Text Filter gRPC server.

    :param service: The TextFilterService which will serve the requests
    :param secure_port: [UNIMPLEMENTED] A secure port to use for hosting the server (default option if specified)
    :param insecure_port: An insecure port to use for hosting the server (only used if secure port is None)
    :param max_workers: The amount of workers the server Tread Pool should use
    :return: The gRPC Server instance
    """
    if not secure_port and not insecure_port:
        raise ConnectionError("Please provide either a secure or unsecure port!")
    server = grpc.server(ThreadPoolExecutor(max_workers=max_workers))
    add_TextFilterServiceServicer_to_server(service, server)
    return _start_server(server, secure=secure_port is not None, port=secure_port or insecure_port)


def _start_server(server: grpc.Server, secure: bool, port: int) -> grpc.Server:
    if secure:
        server.add_secure_port(f'[::]:{port}', server_credentials='TO BE ADDED LATER')
    else:
        server.add_insecure_port(f'[::]:{port}')
    server.start()
    # server.wait_for_termination()
    threading.Thread(target=server.wait_for_termination, daemon=True)  # Allows for shell
    return server
