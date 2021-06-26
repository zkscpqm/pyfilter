from typing import Iterable, Text, Iterator
import grpc
from pyfilter.config.config import Config
from pyfilter.src.transport.proto import (
    TextFilterServiceServicer,
    SingleTextFilterRequest, WebpageFilterRequest, SingleTextFilterResponse, MultiFilterResponse
)
from pyfilter.src.text_filter import TextFilter
from pyfilter.src.transport.web_manager.filter_web_manager_service import TextFilterManagerService
from pyfilter.src.transport.web_manager.server_api import start_server_with_service
from pyfilter.utils.logging import TextFilterLogger


class TextFilterService(TextFilterServiceServicer):

    def __init__(self, any_inclusion_keywords: Iterable[Text], all_inclusion_keywords: Iterable[Text],
                 exclusion_keywords: Iterable[Text], quiet: bool = True,
                 create_web_manager: bool = True):
        """
        GRPC Service implementation for the filter application. This is built by or passed into the server factory.
        For parameter info, see TextFilter
        """

        self.filter: TextFilter = TextFilter.new_filter(
            any_inclusion_keywords=any_inclusion_keywords,
            all_inclusion_keywords=all_inclusion_keywords,
            exclusion_keywords=exclusion_keywords
        )
        self._web_manager = None
        if create_web_manager:
            self._web_manager = self._set_web_manager(quiet)
        self.logger = TextFilterLogger(with_queue=create_web_manager, debug_mode=Config.LOG_DEBUG_MODE, quiet=quiet)

    def _set_web_manager(self, quiet: bool) -> grpc.Server:
        web_manager_service = TextFilterManagerService(self.filter, quiet)
        return start_server_with_service(web_manager_service)

    def SingleFilter(self, request: SingleTextFilterRequest, _) -> SingleTextFilterResponse:
        """
        Unary->Unary API for a single filtering request.

        :param request: A protobuf-defined SingleTextFilterRequest containing a string to pass to the filter.
        :param _: Generic context space required by gRPC. Can ignore
        :return: A protobuf-defined SingleTextFilterResponse containing whether the input string passed the filter
        """
        self.logger.info(f'Received filter request: input="{request.input_string}", casefold:{request.casefold}')
        passed = self.filter.filter(input_string=request.input_string, casefold=request.casefold)
        return SingleTextFilterResponse(passed_filter=passed)

    def MultiFilter(self, request: Iterable[SingleTextFilterRequest], _) -> MultiFilterResponse:
        """
        Stream->Unary API for multiple filtering requests.

        :param request: A stream of protobuf-defined SingleTextFilterRequests containing strings to pass to the filter.
        :param _: Generic context space required by gRPC. Can ignore
        :return: A protobuf-defined MultiFilterResponse containing a list of strings which passed the filter
        """
        self.logger.info(f'Received multi filter request...')
        responses = []
        for filter_req in request:
            self.logger.info(f'Processing filter request: input="{filter_req.input_string}", casefold:{filter_req.casefold}')
            passed = self.filter.filter(input_string=filter_req.input_string, casefold=filter_req.casefold)
            if passed:
                responses.append(filter_req.input_string)
        return MultiFilterResponse(passed_inputs=responses)

    def MultiFilterStream(self, request: Iterator[SingleTextFilterRequest], _) -> Iterator[SingleTextFilterResponse]:
        """
        Stream->Stream API for multiple filtering requests.

        :param request: A stream of protobuf-defined SingleTextFilterRequests containing strings to pass to the filter.
        :param _: Generic context space required by gRPC. Can ignore
        :return: A stream of protobuf-defined SingleTextFilterResponses reflecting which strings passed the filter
        """
        self.logger.info(f'Received multi filter stream request...')
        for filter_req in request:
            self.logger.info(f'Processing filter request: input="{filter_req.input_string}", casefold:{filter_req.casefold}')
            passed = self.filter.filter(input_string=filter_req.input_string, casefold=filter_req.casefold)
            yield SingleTextFilterResponse(passed_filter=passed)

    def WebpageFilter(self, request: WebpageFilterRequest, _) -> SingleTextFilterResponse:
        """
        Unary->Unary API for a single filtering request.

        :param request: A protobuf-defined SingleTextFilterRequest containing a string to pass to the filter.
        :param _: Generic context space required by gRPC. Can ignore
        :return: A protobuf-defined SingleTextFilterResponse containing whether the input string passed the filter
        """
        self.logger.info(f'Received web filter request: url="{request.url}", casefold:{request.casefold}')
        passed = self.filter.webpage_filter(
            url=request.url,
            casefold=request.casefold,
            headers=request.headers,
            params=request.params)
        return SingleTextFilterResponse(passed_filter=passed)

    def __del__(self):
        if self._web_manager:
            self._web_manager.stop(grace=None).wait()
