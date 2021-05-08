from typing import Text, NoReturn
from filters import _BaseFilter
from re import Pattern, RegexFlag, compile as regex_compile


class _RegexMatchFilter(_BaseFilter):

    def __init__(self, regex_pattern: Pattern):
        """
        :param regex_pattern: A compiled regular expression. To use a regex-style string, use the alternate constructor
        """
        super().__init__([])
        self.regex: Pattern = regex_pattern

    def filter(self, input_string, ctx):
        """
        Run a single input through the regex-match filter.

        :param input_string: The value to run through the filter.
        :param ctx: A context with metadata pertaining to this filter request.
        :return: True if the input string matches the regex
        """
        if not self.regex or not self.enabled:
            return True

        if ctx.casefold:
            input_string = input_string.casefold()

        return bool(self.regex.search(input_string))

    def update_pattern(self, regex_string: Text, regex_flag: RegexFlag) -> NoReturn:
        self.regex = regex_compile(regex_string, regex_flag)

    def clear(self) -> NoReturn:
        self.regex = None

    def __str__(self) -> Text:  # pragma: no cover
        return f'[{"ENABLED" if self.enabled else "DISABLED"}] {self.__name}(regex={self.regex})'

    @property
    def __name(self) -> Text:  # pragma: no cover
        return 'RegexMatchFilter'
