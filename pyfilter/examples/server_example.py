import grpc
from pyfilter import start_server_with_service, TextFilterService


def _wait_enter(server: grpc.Server):
    input("Press 'Enter' to exit...\n")
    # Finish current RPC request and shutdown
    server.stop(grace=None).wait()
    exit(0)


def _start_svr():
    available_breeds = {'siamese', 'bengal', 'persian'}
    required_attributes = {'brown', 'friendly', 'healthy'}
    deal_breakers = {'unvaccinated'}
    # Same as the basic example, we want a cat which is one of 'siamese', 'bengal' or 'persian'
    # It should be brown and friendly and healthy.
    # It should NOT be unvaccinated.

    svc = TextFilterService(
        any_inclusion_keywords=available_breeds,
        all_inclusion_keywords=required_attributes,
        exclusion_keywords=deal_breakers,
        quiet=False
    )

    # For now, SSL is not supported. We host the server using out start_server_with_service API.
    # The server will wait on a separate thread (to allow possible shell access?) and listen on the given port.
    return start_server_with_service(svc, insecure_port=8886)


def main():
    server = _start_svr()
    _wait_enter(server)


if __name__ == '__main__':
    main()
