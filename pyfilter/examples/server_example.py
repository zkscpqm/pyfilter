import grpc

from transport import start_server_with_service, TextFilterService


def _wait_enter(server: grpc.Server):
    input("Press 'Enter' to exit...")
    server.stop(grace=None)
    exit(0)


def _start_svr():
    available_breeds = {'siamese', 'bengal', 'persian'}
    required_attributes = {'brown', 'friendly', 'healthy'}
    deal_breakers = {'unvaccinated'}

    svc = TextFilterService(
        any_inclusion_keywords=available_breeds,
        all_inclusion_keywords=required_attributes,
        exclusion_keywords=deal_breakers
    )
    return start_server_with_service(svc, insecure_port=8886)


def main():
    server = _start_svr()
    _wait_enter(server)


if __name__ == '__main__':
    main()
