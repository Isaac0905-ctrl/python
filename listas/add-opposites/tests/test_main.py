import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ([6, 3, 0, -1, -7, 5], -6),
    ([1, 2, 3, 4, 5], -15),
    ([-1, 2, -3, 4, -5], 3),
    ([1, -2, 3, -4, 5], -3),
]


@pytest.mark.parametrize('numbers, expected', testdata)
def test_run(numbers, expected):
    assert main.run(numbers) == expected
