from typing import Text, Iterable, NoReturn, List, TextIO
from filter_context import FilterContext
from filters import AllMatchFilter
from filters import AnyMatchFilter


class TextFilter:

    def __init__(self, any_inclusion_keywords: List[Text],
                 all_inclusion_keywords: List[Text],
                 exclusion_keywords: List[Text]):
        """
        Text filter constructor. Only takes lists. For different iterable types, use the new_filter constructor.

        :param any_inclusion_keywords: A list of keywords where at least one must be contained in the input
        :param all_inclusion_keywords: A list of keywords where all must be contained in the input
        :param exclusion_keywords: A list of keywords where none should be contained in the input
        """

        self.any_inclusion_filter: AnyMatchFilter = AnyMatchFilter(any_inclusion_keywords)
        self.all_inclusion_filter: AllMatchFilter = AllMatchFilter(all_inclusion_keywords)
        self.exclusion_filter: AnyMatchFilter = AnyMatchFilter(exclusion_keywords)
        self.default_context = FilterContext.get_default_context()

    @classmethod
    def new_filter(cls, any_inclusion_keywords: Iterable[Text] = (),
                   all_inclusion_keywords: Iterable[Text] = (),
                   exclusion_keywords: Iterable[Text] = ()) -> 'TextFilter':
        """
        Alternate constructor taking in any iterable types. For parameter details, see __init__
        """
        return TextFilter(
            any_inclusion_keywords=list(any_inclusion_keywords),
            all_inclusion_keywords=list(all_inclusion_keywords),
            exclusion_keywords=list(exclusion_keywords)
        )

    def update_keywords(self, any_inclusion_keywords: Iterable[Text] = (),
                        all_inclusion_keywords: Iterable[Text] = (),
                        exclusion_keywords: Iterable[Text] = ()) -> NoReturn:
        """
        Add new keywords to the filters. This will not replace the existing keywords, but extend them.

        :param any_inclusion_keywords: More any_inclusion_keywords
        :param all_inclusion_keywords: More all_inclusion_keywords
        :param exclusion_keywords: More exclusion_keywords
        """
        self.any_inclusion_filter.extend_keywords(any_inclusion_keywords)
        self.all_inclusion_filter.extend_keywords(all_inclusion_keywords)
        self.exclusion_filter.extend_keywords(exclusion_keywords)

    def set_keywords(self, any_inclusion_keywords: Iterable[Text] = None,
                     all_inclusion_keywords: Iterable[Text] = None,
                     exclusion_keywords: Iterable[Text] = None) -> NoReturn:
        """
        Replace the current filter keywords with new ones. Leaving any field empty will keep the current one.

        :param any_inclusion_keywords: New any_inclusion_keywords
        :param all_inclusion_keywords: New all_inclusion_keywords
        :param exclusion_keywords: New exclusion_keywords
        """

        if any_inclusion_keywords is not None:
            self.any_inclusion_filter.set_keywords(any_inclusion_keywords)
        if all_inclusion_keywords is not None:
            self.all_inclusion_filter.set_keywords(all_inclusion_keywords)
        if exclusion_keywords is not None:
            self.exclusion_filter.set_keywords(exclusion_keywords)

    def delete_keywords(self, any_inclusion_keywords: Iterable[Text] = (),
                        all_inclusion_keywords: Iterable[Text] = (),
                        exclusion_keywords: Iterable[Text] = ()) -> NoReturn:
        """
        Delete keywords in filters if they exist

        :param any_inclusion_keywords: Single_inclusion_keywords to delete
        :param all_inclusion_keywords: Multi_inclusion_keywords to delete
        :param exclusion_keywords: Exclusion_keywords to delete
        """
        self.any_inclusion_filter.delete_keywords(any_inclusion_keywords)
        self.all_inclusion_filter.delete_keywords(all_inclusion_keywords)
        self.exclusion_filter.delete_keywords(exclusion_keywords)

    def _filter(self, input_string: Text, ctx: FilterContext) -> bool:
        """
        See filter method

        :param ctx: A context with metadata pertaining to this filter request.
        """
        ctx = ctx or self.default_context
        if not self.any_inclusion_filter.filter(input_string, ctx):
            return False

        if not self.all_inclusion_filter.filter(input_string, ctx):
            return False

        if self.exclusion_filter.filter(input_string, ctx):
            return False

        return True

    def filter(self, input_string: Text, casefold: bool = True) -> bool:
        """
        Run a single input through the filters.

        :param input_string: The value to run through the filters.
        :param casefold: Should the values be compared without caring about uppercase/lowercase?
        :return: True if: We matched at least one of the single inclusion keywords, all of the multi inclusion keywords,
         none of the exclusion keywords
        Otherwise False.
        """
        ctx = FilterContext(casefold=casefold)
        return self._filter(input_string, ctx)

    def multi_filter(self, input_list: Iterable[Text], casefold: bool = True) -> List[Text]:
        """
        Run the filter on multiple inputs. For more details see filter.

        :param input_list: A list of string inputs
        :param casefold: Should the values be compared without caring about uppercase/lowercase?
        :return: A list of inputs which passed the filtering process.
        """
        ctx = FilterContext(casefold=casefold)
        return [input_string for input_string in input_list if self._filter(input_string, ctx)]

    def file_filter(self, filename: Text, safe: bool = True, casefold: bool = True) -> bool:
        """
        Run the filter on a file.

        :param filename: The name of the file
        :param safe: If this is True, the file will be loaded line by line, instead of all at once.
         Prevents memory overflows and is recommended for larger files.
        :param casefold: Should the values be compared without caring about uppercase/lowercase?
        :return: See _filter method or _safe_file_filter if the safety flag is True.
        """
        ctx = FilterContext(casefold=casefold)
        with open(filename, 'r') as h_file:
            result = self._filter(h_file.read(), ctx) if not safe else self._safe_file_filter(h_file, ctx)
        return result

    def _safe_file_filter(self, file_handle: TextIO, ctx: FilterContext) -> bool:
        """
        A way to run the filter on a file without loading the whole thing in memory

        :param file_handle: A file handle to read safe
        :param ctx: A context with metadata pertaining to this filter request.
        :return: Did the file go through the filters?
        """
        matched_any_single_inclusion_keywords = False
        matched_all_inclusion_keywords_set = set()

        for line in file_handle:
            if not matched_any_single_inclusion_keywords:
                matched_any_single_inclusion_keywords = self.any_inclusion_filter.filter(line, ctx)

            seen_multi_match_keywords = self.all_inclusion_filter.get_all_matching_keywords(line, ctx)
            matched_all_inclusion_keywords_set |= seen_multi_match_keywords

            if self.exclusion_filter.filter(line, ctx):
                return False

        return matched_any_single_inclusion_keywords \
            and self.all_inclusion_filter.all_match(matched_all_inclusion_keywords_set)
