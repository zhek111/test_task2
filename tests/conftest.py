import json
import os

import pytest


def get_fixture_path():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        'fixtures.json')


@pytest.fixture
def matrix_fixtures():
    path = get_fixture_path()
    with open(path) as f:
        return json.load(f)
