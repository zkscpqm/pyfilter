from copy import copy
from typing import Type, NoReturn, List, Text, Union

from pyfilter.src.filter_context import FilterContext
from pyfilter.src.filters import AnyMatchFilter, AllMatchFilter


class BaseFilterTest:

    def set_filter(self, filter_type: Type, keywords: List[Text]) -> NoReturn:
        self.filter: Union[AnyMatchFilter, AllMatchFilter] = filter_type(keywords)

    def test_no_filtering_if_no_keywords(self) -> NoReturn:
        self.filter.set_keywords([])
        ctx = FilterContext.get_default_context()
        cases = [
            'some_string_with_dog',
            'capitalized Cat str',
            'string without those keywords',
            'do g',
            ''
        ]

        for input_string in cases:
            assert self.filter.filter(input_string, ctx) is True

    def test_add_keywords(self) -> NoReturn:
        new_keyword = 'something new'
        old_filter_keywords = copy(self.filter.keywords)
        assert new_keyword not in old_filter_keywords
        self.filter.extend_keywords([new_keyword])
        assert self.filter.keywords == old_filter_keywords + [new_keyword]

    def test_set_keywords(self) -> NoReturn:
        new_keywords = ['new', 'kw', 'list']
        self.filter.set_keywords(new_keywords)
        assert self.filter.keywords == new_keywords

    def test_delete_keywords(self) -> NoReturn:
        deletable_keyword = self.filter.keywords[0]
        self.filter.delete_keywords([deletable_keyword])
        assert deletable_keyword not in self.filter.keywords
