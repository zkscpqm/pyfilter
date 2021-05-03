from transport.proto.filter_service.text_filter_pb2 import (
    SingleTextFilterRequest,
    SingleTextFilterResponse,
    MultiFilterResponse
)
from transport.proto.filter_service.text_filter_pb2_grpc import (
    TextFilterServiceServicer,
    add_TextFilterServiceServicer_to_server
)
