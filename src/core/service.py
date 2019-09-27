import pytest

from src.core.api.api import API


class Service(API):
    def __init__(self):
        super().__init__()
        self._fail = ''

    def is_failed(self):
        if self._fail is not '':
            pytest.fail(self._fail)

    def fail(self, v):
        self._fail += v

    def verify(self, condition):
        if not condition:
            self.fail('--> {} condition is not True \n'.format(condition))
