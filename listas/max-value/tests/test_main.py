import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ([-11, 10, -6, 15, -1], 15),  # positive and negative
    ([-7, -5, -5, -8, -3], -3),  # all negative
    ([7, 3, 19, 12, 8], 19),  # all positive
]


@pytest.mark.parametrize('values, expected', testdata)
def test_run(values, expected):
    assert main.run(values) == expected
