import unittest
from re import compile as regex_compile
from typing import Text

from parameterized import parameterized
from pyfilter.src.filters import RegexMatchFilter
from pyfilter import FilterContext


class TestRegex(unittest.TestCase):

    def setUp(self) -> None:
        self.email_match_regex = regex_compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[^.,;]+[a-zA-Z0-9-.]")
        self.filter = RegexMatchFilter(regex_pattern=self.email_match_regex)
        self.default_context = FilterContext.get_default_context()

    @parameterized.expand([
        ('my_mail@whatever.com', True),
        ('invalidema@il.', False),
        ('weird.but-valid@email.co.uk', True),
        ('double@@gmail.com', False),
        ('doubledot@dd..com', False),
        ('@noname.com', False),
        ('a@b.cd', True),
    ])
    def test_matched_regex_filter(self, email: Text, expected: bool):
        for casefold in (True, False):
            ctx = FilterContext(casefold=casefold)
            print(f'\n{email} - {self.filter.filter(email, ctx)}')
            assert self.filter.filter(email, ctx) is expected

    @parameterized.expand([
            ("Hi, I'm John and this is, my email {email}", True),
            ("His details are: email - {email}, number - 123", True),
            ('12-\\{email}*\n123', True),
            ('Meet me @ the thing. Ok?', False),
        ])
    def test_matches_regex_as_substring(self, input_string: Text, expected: bool):
        input_string = input_string.format(email='my_mail@whatever.com')
        assert self.filter.filter(input_string, self.default_context) is expected

    @parameterized.expand([('424',), ('gsf4',), ('rAndOM',), ('\\?\'/\n\r\t@#$%^&* , .n',)])
    def test_all_pass_without_regex(self, input_string):
        self.filter.clear()
        assert self.filter.filter(input_string, self.default_context) is True
