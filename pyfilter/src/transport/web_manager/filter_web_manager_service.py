from pyfilter.config.config import Config
from pyfilter.src.text_filter import TextFilter
from pyfilter.src.transport.proto import (
    TextFilterManagerServicer,
    Keywords, KeywordsResponse,
    GetKeywordsRequest, SetKeywordsRequest,
    UpdateKeywordsRequest, DeleteKeywordsRequest,
    FilterServerInfoRequest, FilterServerInfoResponse
)
from pyfilter.utils.logging import TextFilterLogger


class TextFilterManagerService(TextFilterManagerServicer):

    def __init__(self, filter_svc: TextFilter, quiet: bool = True):
        self.__filter_svc = filter_svc
        self.logger = TextFilterLogger(with_queue=True, debug_mode=Config.LOG_DEBUG_ENABLED, quiet=quiet)

    def GetKeywords(self, _: GetKeywordsRequest, __) -> KeywordsResponse:
        self.logger.info(f'Received keywords GET request')
        return self._build_response()

    def UpdateKeywords(self, request: UpdateKeywordsRequest, _) -> KeywordsResponse:
        self.logger.info(f'Received keywords UPDATE request')
        self.__filter_svc.update_keywords(
            any_inclusion_keywords=request.keywords.any_keywords,
            all_inclusion_keywords=request.keywords.all_keywords,
            exclusion_keywords=request.keywords.exclusion_keywords,
        )
        return self._build_response()

    def SetKeywords(self, request: SetKeywordsRequest, _) -> KeywordsResponse:
        self.logger.info(f'Received keywords SET request')
        self.__filter_svc.set_keywords(
            any_inclusion_keywords=request.keywords.any_keywords,
            all_inclusion_keywords=request.keywords.all_keywords,
            exclusion_keywords=request.keywords.exclusion_keywords,
            regex_string=request.regex_string
        )
        return self._build_response()

    def DeleteKeywords(self, request: DeleteKeywordsRequest, _) -> KeywordsResponse:
        self.logger.info(f'Received keywords DELETE request')
        self.__filter_svc.delete_keywords(
            any_inclusion_keywords=request.keywords.any_keywords,
            all_inclusion_keywords=request.keywords.all_keywords,
            exclusion_keywords=request.keywords.exclusion_keywords,
            clear_regex=request.clear_regex
        )
        return self._build_response()

    def ServerInfo(self, _: FilterServerInfoRequest, __) -> FilterServerInfoResponse:
        self.logger.info(f'Received server info GET request')
        return FilterServerInfoResponse(
            server_url='localhost',
            server_port=8888,
            server_uptime_seconds=1  # TODO: DO
        )

    def _build_keywords(self) -> Keywords:
        return Keywords(
            any_keywords=self.__filter_svc.any_inclusion_filter.keywords,
            all_keywords=self.__filter_svc.all_inclusion_filter.keywords,
            exclusion_keywords=self.__filter_svc.exclusion_filter.keywords
        )

    def _build_response(self):
        return KeywordsResponse(
            keywords=self._build_keywords(),
            regex_string=self.__filter_svc.regex_filter.keywords
        )
