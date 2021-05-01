import unittest
from typing import Any, List, Text, Type, NoReturn, Set

from filter_context import FilterContext
from text_filter import TextFilter


class TestFilter(unittest.TestCase):

    def setUp(self) -> Any:
        self.single_inclusion_keywords: Set[Text] = {'dog', 'cat'}
        self.multi_inclusion_keywords: Set[Text] = {'plane', 'car'}
        self.exclusion_keywords: Set[Text] = {'red', 'grassy'}
        self.filter = TextFilter.new_filter(
            any_inclusion_keywords=self.single_inclusion_keywords,
            all_inclusion_keywords=self.multi_inclusion_keywords,
            exclusion_keywords=self.exclusion_keywords
        )

    def test_init(self) -> NoReturn:
        self.assertEqual(self.filter.any_inclusion_filter.keywords, list(self.single_inclusion_keywords),
                         'The any_inclusion_keywords are different than the expected LIST of STRINGS of input data')
        self.assertEqual(self.filter.all_inclusion_filter.keywords, list(self.multi_inclusion_keywords),
                         'The all_inclusion_keywords are different than the expected LIST of STRINGS of input data')
        self.assertEqual(self.filter.exclusion_filter.keywords, list(self.exclusion_keywords),
                         'The exclusion_keywords are different than the expected LIST of STRINGS of input data')

        expected_default_context = FilterContext(casefold=True)
        self.assertEqual(self.filter.default_context, expected_default_context,
                         'The default context is different from the expected (casefold=True)')

    def test_update_keywords(self) -> NoReturn:

        new_single_inclusion_keywords = []
        new_multi_inclusion_keywords = []
        new_exclusion_keywords = []
        self.filter.update_keywords(
            any_inclusion_keywords=new_single_inclusion_keywords,
            all_inclusion_keywords=new_multi_inclusion_keywords,
            exclusion_keywords=new_exclusion_keywords
        )
        self.assertEqual(self.filter.any_inclusion_filter.keywords,
                         list(self.single_inclusion_keywords) + list(new_single_inclusion_keywords),
                         'The any_inclusion_keywords are different than the expected LIST of STRINGS of input data')
        self.assertEqual(self.filter.all_inclusion_filter.keywords,
                         list(self.multi_inclusion_keywords) + list(new_multi_inclusion_keywords),
                         'The any_inclusion_keywords are different than the expected LIST of STRINGS of input data')
        self.assertEqual(self.filter.any_inclusion_filter.keywords,
                         list(self.single_inclusion_keywords) + list(new_single_inclusion_keywords),
                         'The any_inclusion_keywords are different than the expected LIST of STRINGS of input data')