import os
from typing import Text, Any, Iterable


class ConfigMeta(type):
    """
    Metaclass which checks environment variables for config attributes if they don't exist
    """

    def __getattr__(cls, item: Text) -> Any:
        if value := os.getenv(item):
            setattr(cls, item, value)
            return value


class BaseConfig(metaclass=ConfigMeta):

    def __init__(self, *args, **kwargs):
        raise Exception("Config classes should not be initialized!")

    any_inclusion_keywords: Iterable[Text] = ()
    all_inclusion_keywords: Iterable[Text] = ()
    exclusion_keywords: Iterable[Text] = ()
    default_casefold_option: bool
