import unittest
from typing import Any, Text, List
from parameterized import parameterized

from pyfilter.src.filter_context import FilterContext
from pyfilter.src.filters import AllMatchFilter
from pyfilter.test.base_filter_test import BaseFilterTest


class TestAllMatchFilter(unittest.TestCase, BaseFilterTest):

    def setUp(self) -> Any:
        self.keywords: List[Text] = ['dog', 'cat']
        self.set_filter(AllMatchFilter, self.keywords)

    @parameterized.expand([(True,), (False,)])
    def test_matched_all_inclusion_filters(self, ctx_casefold: bool) -> Any:
        ctx = FilterContext(casefold=ctx_casefold)
        cases = [
            ('some_string_with_dog', False),
            ('string without those keywords', False),
            ('dogs and cats are cool', True),
        ]

        for input_string, expected in cases:
            assert self.filter.filter(input_string, ctx) is expected

    @parameterized.expand([(True,), (False,)])
    def test_get_all_matching_inclusion_keywords(self, ctx_casefold: bool) -> Any:
        ctx = FilterContext(casefold=ctx_casefold)
        cases = [
            ('some_string_with_dog', {'dog'}, False),
            ('string without those keywords', set(), False),
            ('dogs and cats are cool', {'dog', 'cat'}, True),
        ]
        for input_string, expected, all_match in cases:
            matching = self.filter.get_all_matching_keywords(input_string, ctx)
            assert matching == expected
            assert self.filter.all_match(matching) == all_match
