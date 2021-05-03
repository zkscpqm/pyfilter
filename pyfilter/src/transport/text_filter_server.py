from typing import Iterable, Text, Iterator

from transport.proto import (
    TextFilterServiceServicer,
    SingleTextFilterRequest, SingleTextFilterResponse, MultiFilterResponse
)
from text_filter import TextFilter


class TextFilterServer(TextFilterServiceServicer):

    def __init__(self, any_inclusion_keywords: Iterable[Text],
                 all_inclusion_keywords: Iterable[Text], exclusion_keywords: Iterable[Text]):
        self.filter = TextFilter.new_filter(
            any_inclusion_keywords=any_inclusion_keywords,
            all_inclusion_keywords=all_inclusion_keywords,
            exclusion_keywords=exclusion_keywords
        )

    def SingleFilter(self, request: SingleTextFilterRequest, _) -> SingleTextFilterResponse:
        passed = self.filter.filter(input_string=request.input_string, casefold=request.casefold)
        return SingleTextFilterResponse(passed_filter=passed)

    def MultiFilter(self, request: Iterator[SingleTextFilterRequest], _) -> MultiFilterResponse:

        responses = []
        for filter_req in request:
            passed = self.filter.filter(input_string=filter_req.input_string, casefold=filter_req.casefold)
            if passed:
                responses.append(filter_req.input_string)
        return MultiFilterResponse(passed_inputs=responses)

    def MultiFilterStream(self, request: Iterator[SingleTextFilterRequest], _) -> Iterator[SingleTextFilterResponse]:
        for filter_req in request:
            passed = self.filter.filter(input_string=filter_req.input_string, casefold=filter_req.casefold)
            yield SingleTextFilterResponse(passed_filter=passed)
