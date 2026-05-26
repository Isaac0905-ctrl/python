import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ([6, 3, 0, -1, -7, 5], 14),
    ([1, -4, 7, 12], 20),
    ([-1, -1, -1, -1, -1, -1], 0),
    ([1, -1, 2, -2, 3, -3, 4, -4, 5, -5], 15),
    ([], 0),
]


@pytest.mark.parametrize('numbers, expected', testdata)
def test_run(numbers, expected):
    assert main.run(numbers) == expected
