from typing import Final


class FilterContext:

    __slots__ = ['casefold']

    def __init__(self, casefold: bool):
        self.casefold: Final[bool] = casefold

    @classmethod
    def get_default_context(cls) -> 'FilterContext':
        return FilterContext(
            casefold=True
        )

    def __eq__(self, other: 'FilterContext') -> bool:
        return (
            self.casefold == other.casefold
        )
