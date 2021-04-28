from typing import Text, List

from pyfilter.src.base_filter import BaseFilter


class SingleMatchFilter(BaseFilter):

    def __init__(self, keywords: List[Text]):
        super().__init__(keywords)

    def filter(self, input_string, ctx):
        """
        Run a single input through the single-inclusion filter.

        :param input_string: The value to run through the filter.
        :param ctx: A context with metadata pertaining to this filter request.
        :return: True if any of the SingleInclusionFilter keywords was matched, otherwise False
        """
        if not self.keywords:
            return True

        for keyword in self.keywords:
            if ctx.casefold:
                keyword = keyword.casefold()
                input_string = input_string.casefold()
            if keyword in input_string:
                return True
        return False
