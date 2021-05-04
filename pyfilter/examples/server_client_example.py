from transport import start_server_with_service, TextFilterService
import threading


def _start_svr():
    available_breeds = {'siamese', 'bengal', 'persian'}
    required_attributes = {'brown', 'friendly', 'healthy'}
    deal_breakers = {'unvaccinated'}

    svc = TextFilterService(
        any_inclusion_keywords=available_breeds,
        all_inclusion_keywords=required_attributes,
        exclusion_keywords=deal_breakers
    )
    start_server_with_service(svc, insecure_port=8886)


def main():
    server_thread = threading.Thread(target=_start_svr, daemon=True)
    server_thread.start()


if __name__ == '__main__':
    main()
