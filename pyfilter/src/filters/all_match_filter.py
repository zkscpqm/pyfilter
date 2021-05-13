from typing import Text, List, Set
from pyfilter.src.filters import _BaseFilter
from pyfilter.src.filter_context import FilterContext


class _AllMatchFilter(_BaseFilter):

    def __init__(self, keywords: List[Text]):
        super().__init__(keywords)

    def filter(self, input_string, ctx):
        """
        Run a single input through the all-match filters.

        :param input_string: The value to run through the filters.
        :param ctx: A context with metadata pertaining to this filter request.
        :return: True if all of the AllMatchFilter keywords were matched, otherwise False
        """
        if not self.keywords or not self.enabled:
            return True

        for whitelist_keyword in self.keywords:
            if ctx.casefold:
                whitelist_keyword = whitelist_keyword.casefold()
                input_string = input_string.casefold()
            if whitelist_keyword not in input_string:
                return False
        return True

    def get_all_matching_keywords(self, input_string: Text, ctx: FilterContext) -> Set[Text]:
        """
        Returns all keywords which are seen in the input string.

        :param input_string: The value to run through the filter.
        :param ctx: A context with metadata pertaining to this filter request.
        :return: A set of whitelist_keywords existing in the input_string and the filter's keywords
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
        """
        Checks whether an input set matches all keywords

        :param keywords: A set of items to check
        :return: True if the sets are identical, otherwise False
        """
        return keywords == set(self.keywords)

    @property
    def __name(self) -> Text:  # pragma: no cover
        return 'AllMatchFilter'
