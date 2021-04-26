from typing import Text, Iterable, NoReturn, List, TextIO, Set

from pyfilter.src.filter_context import FilterContext


class TextFilter:

    def __init__(self, single_inclusion_filters: List[Text],
                 multi_inclusion_filters: List[Text],
                 exclusion_filters: List[Text]):
        """
        Text filter constructor. Only takes lists. For different iterable types, use the new_filter constructor.

        :param single_inclusion_filters: A list of keywords where at least one must be contained in the input
        :param multi_inclusion_filters: A list of keywords where all must be contained in the input
        :param exclusion_filters: A list of keywords where none should be contained in the input
        """

        self.single_inclusion_filters: List[Text] = single_inclusion_filters
        self.multi_inclusion_filters: List[Text] = multi_inclusion_filters
        self.exclusion_filters: List[Text] = exclusion_filters
        self.default_context = FilterContext.get_default_context()

    @classmethod
    def new_filter(cls, single_inclusion_filters: Iterable[Text] = (),
                   multi_inclusion_filters: Iterable[Text] = (),
                   exclusion_filters: Iterable[Text] = ()) -> 'TextFilter':
        """
        Alternate constructor taking in any iterable types. For parameter details, see __init__
        """
        return TextFilter(
            single_inclusion_filters=list(single_inclusion_filters),
            multi_inclusion_filters=list(multi_inclusion_filters),
            exclusion_filters=list(exclusion_filters)
        )

    def update_filters(self, single_inclusion_filters: Iterable[Text] = (),
                       multi_inclusion_filters: Iterable[Text] = (),
                       exclusion_filters: Iterable[Text] = ()) -> NoReturn:
        """
        Add new keywords to the filters. This will not replace the existing filters, but extend them.

        :param single_inclusion_filters: More single_inclusion_filters
        :param multi_inclusion_filters: More multi_inclusion_filters
        :param exclusion_filters: More exclusion_filters
        """
        self.single_inclusion_filters.extend(single_inclusion_filters)
        self.multi_inclusion_filters.extend(multi_inclusion_filters)
        self.exclusion_filters.extend(exclusion_filters)

    def _filter(self, input_string: Text, ctx: FilterContext) -> bool:
        ctx = ctx or self.default_context
        if not self.matched_any_single_inclusion_filters(input_string, ctx):
            return False

        if not self.matched_all_multi_inclusion_filters(input_string, ctx):
            return False

        if self.matched_any_exclusion_filters(input_string, ctx):
            return False

        return True

    def filter(self, input_string: Text, casefold: bool = True) -> bool:
        """
        Run a single input through the filters.

        :param input_string: The value to run through the filters.
        :param casefold: Should the values be compared without caring about uppercase/lowercase?
        :return: True if
         - We matched at least one of the single_inclusion_filters
         - All of the multi_inclusion_filters
         - None of the exclusion_filters
        Otherwise False.
        """
        ctx = FilterContext(casefold=casefold)
        return self._filter(input_string, ctx)

    def multi_filter(self, input_list: Iterable[Text], casefold: bool = True) -> List[Text]:
        """
        Run the filter on multiple inputs. For more details see filter.

        :param input_list: A list of string inputs
        :param casefold: Should values be casefolded? (If True, Upper/Lowercase is ignored)
        :return: A list of inputs which passed the filtering process.
        """
        ctx = FilterContext(casefold=casefold)
        return [input_string for input_string in input_list if self._filter(input_string, ctx)]

    def file_filter(self, filename: Text, safe: bool = True, casefold: bool = True) -> bool:
        ctx = FilterContext(casefold=casefold)
        with open(filename, 'r') as h_file:
            result = self._filter(h_file.read(), ctx) if not safe else self._safe_file_filter(h_file, ctx)
        return result

    def _safe_file_filter(self, file_handle: TextIO, ctx: FilterContext) -> bool:
        """
        A way to run the fliter on a file without loading the whole thing in memory

        :param file_handle: A file handle to read safely from
        :param ctx: A context with metadata pertaining to this filter request.
        :return: Did the file go through the filters?
        """
        matched_any_single_inclusion_filters = False
        matched_multi_inclusion_filters_set = set()

        for line in file_handle:
            if not matched_any_single_inclusion_filters:
                matched_any_single_inclusion_filters = self.matched_any_single_inclusion_filters(line, ctx)

            seen_multi_match_keywords = self._get_all_matching_multi_inclusion_keywords(line, ctx)
            matched_multi_inclusion_filters_set |= seen_multi_match_keywords

            if self.matched_any_exclusion_filters(line, ctx):
                return False

        return matched_any_single_inclusion_filters \
               and matched_multi_inclusion_filters_set == set(self.multi_inclusion_filters)

    def _get_all_matching_multi_inclusion_keywords(self, input_string: Text, ctx: FilterContext) -> Set[Text]:
        """
        Returns all keywords from multi_inclusion_filters which are seen in the input string.

        :param input_string: The value to run through the filters.
        :param ctx: A context with metadata pertaining to this filter request.
        :return: A set of whitelist_keywords existing in the input_string and multi_inclusion_filters
        """
        seen = set()
        for whitelist_keyword in self.multi_inclusion_filters:
            if ctx.casefold:
                whitelist_keyword = whitelist_keyword.casefold()
                input_string = input_string.casefold()
            if whitelist_keyword in input_string:
                seen.add(whitelist_keyword)
        return seen

    def matched_any_single_inclusion_filters(self, input_string: Text, ctx: FilterContext) -> bool:
        """
        Run a single input through the single-inclusion filters.

        :param input_string: The value to run through the filters.
        :param ctx: A context with metadata pertaining to this filter request.
        :return: True if any of the single_inclusion_filter keywords was matched, otherwise False
        """
        if not self.single_inclusion_filters:
            return True

        for whitelist_keyword in self.single_inclusion_filters:
            if ctx.casefold:
                whitelist_keyword = whitelist_keyword.casefold()
                input_string = input_string.casefold()
            if whitelist_keyword in input_string:
                return True
        return False

    def matched_all_multi_inclusion_filters(self, input_string: Text, ctx: FilterContext) -> bool:
        """
        Run a single input through the multi-inclusion filters.

        :param input_string: The value to run through the filters.
        :param ctx: A context with metadata pertaining to this filter request.
        :return: True if all of the multi_inclusion_filter keywords were matched, otherwise False
        """
        if not self.multi_inclusion_filters:
            return True

        for whitelist_keyword in self.multi_inclusion_filters:
            if ctx.casefold:
                whitelist_keyword = whitelist_keyword.casefold()
                input_string = input_string.casefold()
            if whitelist_keyword not in input_string:
                return False
        return True

    def matched_any_exclusion_filters(self, input_string: Text, ctx: FilterContext) -> bool:
        """
        Run a single input through the exclusion filters.

        :param input_string: The value to run through the filters.
        :param ctx: A context with metadata pertaining to this filter request.
        :return: True if any of the exclusion_filter keywords were matched, otherwise False
        """
        if not self.exclusion_filters:
            return False

        for blacklist_keyword in self.exclusion_filters:
            if ctx.casefold:
                blacklist_keyword = blacklist_keyword.casefold()
                input_string = input_string.casefold()
            if blacklist_keyword in input_string:
                return True
        return False
