from typing import Text, List, Iterable, NoReturn

from pyfilter.src.filter_context import FilterContext


class BaseFilter:

    def __init__(self, keywords: List[Text]):
        self.keywords: List[Text] = keywords

    def filter(self, input_string: Text, ctx: FilterContext) -> bool:
        """
        Run a input through the filter.

        :param input_string: The value to run through the filter.
        :param ctx: A context with metadata pertaining to this filter request.
        :return: Return whether the filter conditions were met
        """
        raise NotImplementedError

    def extend_keywords(self, extension: Iterable[Text]) -> NoReturn:
        """
        Add new keywords to the keywords. This will not replace the existing keywords, but extend them.

        :param extension: Keywords to add
        """
        self.keywords.extend(extension)

    def set_keywords(self, new_keywords: Iterable[Text]) -> NoReturn:
        """
        Replace the current filters with new ones.

        :param new_keywords: New keywords
        """
        self.keywords = list(new_keywords)

    def delete_keywords(self, keywords_to_delete: Iterable[Text]) -> NoReturn:
        """
        Delete keywords in the filter, if they exist

        :param keywords_to_delete: The keywords to remove from the filter
        """
        for keyword in keywords_to_delete:
            # Using 'while' to handle multiple occurrences of the keyword in the filter list
            while keyword in self.keywords:
                self.keywords.remove(keyword)
