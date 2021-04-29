import unittest
from typing import Any, Text, List
from parameterized import parameterized

from pyfilter.src.filter_context import FilterContext
from pyfilter.src.filters import MultiMatchFilter
from pyfilter.test.base_filter_test import BaseFilterTest


class TestMultiMatchFilter(unittest.TestCase, BaseFilterTest):

    def setUp(self) -> Any:
        self.keywords: List[Text] = ['dog', 'cat']
        self.set_filter(MultiMatchFilter, self.keywords)

    @parameterized.expand([("casefolded_true", True), ("casefolded_false", False)])
    def test_matched_all_multi_inclusion_filters(self, _, ctx_casefold: bool) -> Any:
        ctx = FilterContext(casefold=ctx_casefold)
        cases = [
            ('some_string_with_dog', False),
            ('string without those keywords', False),
            ('dogs and cats are cool', True),
        ]

        for input_string, expected in cases:
            assert self.filter.filter(input_string, ctx) is expected

    @parameterized.expand([("casefolded_true", True), ("casefolded_false", False)])
    def test_get_all_matching_multi_inclusion_keywords(self, _, ctx_casefold: bool) -> Any:
        ctx = FilterContext(casefold=ctx_casefold)
        cases = [
            ('some_string_with_dog', {'dog'}, False),
            ('string without those keywords', set(), False),
            ('dogs and cats are cool', {'dog', 'cat'}, True),
        ]
        for input_string, expected, all_match in cases:
            matching = self.filter.get_all_matching_multi_inclusion_keywords(input_string, ctx)
            assert matching == expected
            assert self.filter.all_match(matching) == all_match
