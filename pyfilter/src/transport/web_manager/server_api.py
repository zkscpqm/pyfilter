import threading
from concurrent.futures import ThreadPoolExecutor
import grpc
from pyfilter.src.transport.proto import add_TextFilterManagerServicer_to_server
from pyfilter.src.transport.web_manager.filter_web_manager_service import TextFilterManagerService


def start_server_with_service(service: TextFilterManagerService) -> grpc.Server:
    """
    A bootstrap API to start the Text Filter gRPC web server.

    :param service: The TextFilterManagerService which will manage the Filter
    :return: The gRPC Server instance
    """
    server = grpc.server(ThreadPoolExecutor(max_workers=10))  # TODO: Get from config
    add_TextFilterManagerServicer_to_server(service, server)
    return _start_server(server, port=9123)  # TODO: Get from config


def _start_server(server: grpc.Server, port: int) -> grpc.Server:
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    threading.Thread(name="TextFilter Server Manager Thread",target=server.wait_for_termination, daemon=True).start()
    return server
