import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ([6, 2, 1, 8, 10], 16),
    ([1, 1, 11, 2, 3], 5),
    ([7, 12, 4, 9, 3], 20),
    ([1], 0),
    ([1, 1], 0),
    ([1, 2], 0),
    ([], 0),
]


@pytest.mark.parametrize('values, expected', testdata)
def test_run(values, expected):
    assert main.run(values) == expected
