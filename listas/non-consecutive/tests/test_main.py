import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ([1, 2, 3, 4, 6, 7, 8], 6),
    ([101, 102, 103], None),
    ([-5, -4, -3, 0, 3, 4, 5], 0),
    ([1], None),
    ([], None),
]


@pytest.mark.parametrize('values, expected', testdata)
def test_run(values, expected):
    assert main.run(values) == expected
