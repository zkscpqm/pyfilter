from typing import Iterable, Text, Iterator

from pyfilter.src.transport.proto import (
    TextFilterServiceServicer,
    SingleTextFilterRequest, WebpageFilterRequest, SingleTextFilterResponse, MultiFilterResponse
)
from pyfilter.src.text_filter import TextFilter


class TextFilterService(TextFilterServiceServicer):

    def __init__(self, any_inclusion_keywords: Iterable[Text], all_inclusion_keywords: Iterable[Text],
                 exclusion_keywords: Iterable[Text], quiet: bool = True):
        """
        GRPC Service implementation for the filter application. This is built by or passed into the server factory.
        For parameter info, see TextFilter
        """

        self.filter: TextFilter = TextFilter.new_filter(
            any_inclusion_keywords=any_inclusion_keywords,
            all_inclusion_keywords=all_inclusion_keywords,
            exclusion_keywords=exclusion_keywords
        )
        self.quiet = quiet  # TODO: Pass this to the logger instead!

    def SingleFilter(self, request: SingleTextFilterRequest, _) -> SingleTextFilterResponse:
        """
        Unary->Unary API for a single filtering request.

        :param request: A protobuf-defined SingleTextFilterRequest containing a string to pass to the filter.
        :param _: Generic context space required by gRPC. Can ignore
        :return: A protobuf-defined SingleTextFilterResponse containing whether the input string passed the filter
        """
        if not self.quiet:
            print(f'Received filter request: input="{request.input_string}", casefold:{request.casefold}')
        passed = self.filter.filter(input_string=request.input_string, casefold=request.casefold)
        return SingleTextFilterResponse(passed_filter=passed)

    def MultiFilter(self, request: Iterable[SingleTextFilterRequest], _) -> MultiFilterResponse:
        """
        Stream->Unary API for multiple filtering requests.

        :param request: A stream of protobuf-defined SingleTextFilterRequests containing strings to pass to the filter.
        :param _: Generic context space required by gRPC. Can ignore
        :return: A protobuf-defined MultiFilterResponse containing a list of strings which passed the filter
        """
        if not self.quiet:
            print(f'Received multi filter request...')
        responses = []
        for filter_req in request:
            if not self.quiet:
                print(f'Processing filter request: input="{filter_req.input_string}", casefold:{filter_req.casefold}')
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
        if not self.quiet:
            print(f'Received multi filter stream request...')
        for filter_req in request:
            if not self.quiet:
                print(f'Processing filter request: input="{filter_req.input_string}", casefold:{filter_req.casefold}')
            passed = self.filter.filter(input_string=filter_req.input_string, casefold=filter_req.casefold)
            yield SingleTextFilterResponse(passed_filter=passed)

    def WebpageFilter(self, request: WebpageFilterRequest, _) -> SingleTextFilterResponse:
        """
        Unary->Unary API for a single filtering request.

        :param request: A protobuf-defined SingleTextFilterRequest containing a string to pass to the filter.
        :param _: Generic context space required by gRPC. Can ignore
        :return: A protobuf-defined SingleTextFilterResponse containing whether the input string passed the filter
        """
        if not self.quiet:
            print(f'Received web filter request: url="{request.url}", casefold:{request.casefold}')
        passed = self.filter.webpage_filter(
            url=request.url,
            casefold=request.casefold,
            headers=request.headers,
            params=request.params)
        return SingleTextFilterResponse(passed_filter=passed)
