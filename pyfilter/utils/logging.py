import traceback
from datetime import datetime
from typing import List, Text

from pyfilter.config.config import Config


class _LogMessageQueue:

    def __init__(self):
        self._queue: List[Text] = []
        self.len = 0
        self.max_size = Config.LOG_MSG_QUEUE_MAX_SIZE

    def push(self, log_message: Text):
        while self.len >= self.max_size:
            self.poll()
        self._queue.append(log_message)
        self.len += 1

    def poll(self) -> Text:
        if self.len > 0:
            self.len -= 1
            return self._queue.pop(0)


log_message_queue = _LogMessageQueue()


class TextFilterLogger:
    def __init__(self, with_queue: bool = True, debug_mode: bool = False, quiet: bool = False):
        self.quiet = quiet
        self.debug_mode = debug_mode
        self.with_queue = with_queue

    @classmethod
    def _build_message(cls, msg, level):
        return f'[{datetime.now().time()}][{level}] {msg}'

    def exception(self, msg, *calls):
        msg = self._build_message(msg, 'EXCEPTION')
        self._log(msg, *calls, err=True)

    def warning(self, msg):
        msg = self._build_message(msg, 'WARNING')
        self._log(msg)

    def info(self, msg):
        msg = self._build_message(msg, 'INFO')
        self._log(msg)

    def debug(self, msg):
        if self.debug_mode:
            msg = self._build_message(msg, 'DEBUG')
            self._log(msg)

    def _log(self, msg, *calls, err=False):
        if not self.quiet:
            if err:
                msg = f'{traceback.format_exc()}\n{msg}'
            if calls:
                msg += '\nCalled with:\n' + '\n'.join([str(x) for x in calls])

            if self.with_queue:
                log_message_queue.push(msg)

            print(msg)
