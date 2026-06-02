import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ({'a': 1, 'b': 2}, {'a': 3, 'c': 4}, {'a': 3, 'b': 2, 'c': 4}),
    ({0: 1, 1: 0}, {0: 0, 1: 1}, {0: 0, 1: 1}),
    ({}, {'x': 2.1, 'y': 3.4}, {'x': 2.1, 'y': 3.4}),
    ({}, {}, {}),
]


@pytest.mark.parametrize('d1, d2, expected', testdata)
def test_run(d1, d2, expected):
    assert main.run(d1, d2) == expected
