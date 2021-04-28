from typing import Text, List, Set

from pyfilter.src.base_filter import BaseFilter
from pyfilter.src.filter_context import FilterContext


class MultiMatchFilter(BaseFilter):

    def __init__(self, keywords: List[Text]):
        super().__init__(keywords)

    def filter(self, input_string, ctx):
        """
        Run a single input through the multi-inclusion filters.

        :param input_string: The value to run through the filters.
        :param ctx: A context with metadata pertaining to this filter request.
        :return: True if all of the MultiInclusionFilter keywords were matched, otherwise False
        """
        if not self.keywords:
            return True

        for whitelist_keyword in self.keywords:
            if ctx.casefold:
                whitelist_keyword = whitelist_keyword.casefold()
                input_string = input_string.casefold()
            if whitelist_keyword not in input_string:
                return False
        return True

    def get_all_matching_multi_inclusion_keywords(self, input_string: Text, ctx: FilterContext) -> Set[Text]:
        """
        Returns all keywords from multi_inclusion_keywords which are seen in the input string.

        :param input_string: The value to run through the filters.
        :param ctx: A context with metadata pertaining to this filter request.
        :return: A set of whitelist_keywords existing in the input_string and multi_inclusion_keywords
        """
        seen = set()
        for whitelist_keyword in self.keywords:
            if ctx.casefold:
                whitelist_keyword = whitelist_keyword.casefold()
                input_string = input_string.casefold()
            if whitelist_keyword in input_string:
                seen.add(whitelist_keyword)
        return seen

    def all_match(self, keywords: Set[Text]) -> bool:
        return keywords == set(self.keywords)
