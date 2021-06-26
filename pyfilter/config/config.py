from pyfilter.config.base_config import BaseConfig


class Config(BaseConfig):

    # Logging

    LOG_DEBUG_ENABLED: bool = True
    LOG_MSG_QUEUE_MAX_SIZE: int = 1000

    # Filter Server

    DEFAULT_PORT: int = 8080
