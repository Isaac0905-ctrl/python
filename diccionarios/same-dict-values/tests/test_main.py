import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ({'a': 1, 'b': 1, 'c': 1, 'd': 1}, True),
    ({'a': 1, 'b': 2, 'c': 3, 'd': 4}, False),
    ({1: 'a', 2: 'b', 3: 'c', 4: 'd'}, False),
    ({1: 'a', 2: 'a', 3: 'a', 4: 'a'}, True),
    ({}, True),
]


@pytest.mark.parametrize('items, expected', testdata)
def test_run(items, expected):
    assert main.run(items) == expected
