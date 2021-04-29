from typing import Any, List, Text
import unittest

from parameterized import parameterized

from pyfilter.src.filter_context import FilterContext
from pyfilter.src.filters import SingleMatchFilter
from pyfilter.test.base_filter_test import BaseFilterTest


class TestSingleMatchFilter(unittest.TestCase, BaseFilterTest):

    def setUp(self) -> Any:
        self.keywords: List[Text] = ['dog', 'cat']
        self.set_filter(SingleMatchFilter, self.keywords)

    @parameterized.expand([
        ("casefolded_true", True),
        ("casefolded_false", False)
    ])
    def test_matched_anySingle_inclusion_filters(self, _, ctx_casefold: bool) -> Any:
        ctx = FilterContext(casefold=ctx_casefold)
        cases = [
            ('some_string_with_dog', True),
            ('capitalized Cat str', ctx_casefold),  # Only match True if casefold is on, else False since cat != Cat
            ('string without those keywords', False),
            ('do g', False),
            ('strwithDogandCatasone', ctx_casefold)
        ]

        for input_string, expected in cases:
            assert self.filter.filter(input_string, ctx) is expected
