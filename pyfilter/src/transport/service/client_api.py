from pyfilter.src.transport.service.text_filter_client import TextFilterClient


def get_new_client(secure_port: int = None, insecure_port: int = None, quiet: bool = True):
    if not secure_port and not insecure_port:
        raise ConnectionError("Please provide either a secure or unsecure port!")
    return TextFilterClient.new(secure_port, insecure_port, quiet)
