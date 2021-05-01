import unittest
import os
from typing import Any, Text, NoReturn, Set, Union

from parameterized import parameterized

from filter_context import FilterContext
from text_filter import TextFilter


class TestFilter(unittest.TestCase):

    def setUp(self) -> Any:
        self.single_inclusion_keywords: Set[Text] = {'dog', 'cat'}
        self.multi_inclusion_keywords: Set[Text] = {'plane', 'car'}
        self.exclusion_keywords: Set[Text] = {'red', 'grassy'}
        self.filter: TextFilter = TextFilter.new_filter(
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
        self.assertEqual(self.filter.exclusion_filter.keywords,
                         list(self.exclusion_keywords) + list(new_exclusion_keywords),
                         'The any_inclusion_keywords are different than the expected LIST of STRINGS of input data')

    @parameterized.expand([(['new_exclusion', 'kw'],),
                           (None,)])
    def test_set_keywords(self, new_exclusion_keywords: Union[Text, None]):
        new_single_inclusion_keywords = ['new', 'keywords']
        new_multi_inclusion_keywords = []
        self.filter.set_keywords(
            any_inclusion_keywords=new_single_inclusion_keywords,
            all_inclusion_keywords=new_multi_inclusion_keywords,
            exclusion_keywords=new_exclusion_keywords
        )
        self.assertEqual(self.filter.any_inclusion_filter.keywords,
                         new_single_inclusion_keywords,
                         'The any_inclusion_keywords are different than the expected LIST of STRINGS of input data')
        self.assertEqual(self.filter.all_inclusion_filter.keywords,
                         [],
                         'The any_inclusion_keywords are different than the expected LIST of STRINGS of input data')
        self.assertEqual(self.filter.exclusion_filter.keywords,
                         new_exclusion_keywords or list(self.exclusion_keywords),
                         'The any_inclusion_keywords are different than the expected LIST of STRINGS of input data')

    def test_delete_keywords(self) -> NoReturn:
        single_inclusion_keywords_to_delete = ['dog']
        multi_inclusion_keywords_to_delete = ['nonexistent']

        self.filter.delete_keywords(
            any_inclusion_keywords=single_inclusion_keywords_to_delete,
            all_inclusion_keywords=multi_inclusion_keywords_to_delete,
        )
        self.assertEqual(self.filter.any_inclusion_filter.keywords,
                         ['cat'],
                         'The any_inclusion_keywords are different than the expected LIST of STRINGS of input data')
        self.assertEqual(self.filter.all_inclusion_filter.keywords,
                         list(self.multi_inclusion_keywords),
                         'The any_inclusion_keywords are different than the expected LIST of STRINGS of input data')
        self.assertEqual(self.filter.exclusion_filter.keywords,
                         list(self.exclusion_keywords),
                         'The any_inclusion_keywords are different than the expected LIST of STRINGS of input data')

    @parameterized.expand([("Planes and cars don't allow dogs", True, False),
                           ("Dogs and cats but not the other keywords", False, False),
                           ("Well we have a cat in the car but on on the red plane", False, False),
                           ("The plane carries cats and cars", True, True),
                           ("Just a car and a plane but no pets", False, False)])
    def test_singular_filter(self, input_string: Text,
                             expected_with_casefold: bool, expected_without_casefold: bool):

        self.assertEqual(self.filter.filter(input_string, casefold=True), expected_with_casefold)
        self.assertEqual(self.filter.filter(input_string, casefold=False), expected_without_casefold)

    def test_multi_filter(self):
        input_list = ['cat plane car', 'dog cat', 'cat plane car grassy', '']
        result = self.filter.multi_filter(input_list)
        expected_result = ['cat plane car']
        self.assertEqual(result, expected_result)

    @parameterized.expand([('passing_file.txt', True, True),
                           ('casefold_passing_file.txt', True, False),
                           ('failing_file_1.txt', False, False),
                           ('failing_file_2.txt', False, False),
                           ('failing_file_3.txt', False, False)])
    def test_file_filter(self, filename: Text,
                         expected_with_casefold: bool, expected_without_casefold: bool):
        fp = os.path.join('test_files', filename)

        for casefold in (True, False):
            for safe in (True, False):

                result = self.filter.file_filter(fp, safe=safe, casefold=casefold)
                expected = expected_with_casefold if casefold else expected_without_casefold
                self.assertEqual(result, expected)



