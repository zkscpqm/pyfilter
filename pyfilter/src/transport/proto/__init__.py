from pyfilter.src.transport.proto.filter_service.text_filter_pb2 import (
    SingleTextFilterRequest,
    SingleTextFilterResponse,
    MultiFilterResponse,
    WebpageFilterRequest
)
from pyfilter.src.transport.proto.filter_service.text_filter_pb2_grpc import (
    TextFilterServiceServicer,
    add_TextFilterServiceServicer_to_server,
    TextFilterServiceStub
)

from pyfilter.src.transport.proto.filter_service.filter_web_api_pb2 import (
    GetKeywordsRequest,
    SetKeywordsRequest,
    UpdateKeywordsRequest,
    DeleteKeywordsRequest,
    KeywordsResponse,
    Keywords,
    FilterServerInfoRequest,
    FilterServerInfoResponse
)

from pyfilter.src.transport.proto.filter_service.filter_web_api_pb2_grpc import (
    TextFilterManagerServicer,
    add_TextFilterManagerServicer_to_server,
    TextFilterManagerStub
)
