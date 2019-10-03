import json
from os.path import join
from pathlib import Path

import pytest
from jsonschema import validate

from src.core.api import API


class Service(API):
    def __init__(self):
        super().__init__()
        self._fail = ''
        self._schemas_dir = '{}/services/'.format(Path(__file__).parent.parent)

    def is_failed(self):
        if self._fail is not '':
            pytest.fail(self._fail)

    def fail(self, v):
        self._fail += v

    def verify(self, condition=None, *args):
        # expects that args[0] == actual value
        # args[1] == expected value
        # args[2] == key of verification
        if condition is None:
            if args[0] != args[1]:
                self.fail('--> verify key: {}, '
                          'actual value: {} is not equal to expected: {}'.format(args[2], args[0], args[1]))

        else:
            if not condition:
                self.fail('--> condition is not True')

    def _set_schemas_dir(self, value):
        self._schemas_dir += value

    def get_schemas_dir(self):
        return self._schemas_dir

    def _load_json_schema(self, filename):

        absolute_path = join(self.get_schemas_dir(), filename)

        with open(absolute_path) as schema_file:
            return json.loads(schema_file.read())

    def verify_json_schema(self, data, schema_file):

        schema = self._load_json_schema(schema_file)
        return validate(data, schema)
