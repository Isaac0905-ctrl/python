import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ([1, 2, 3, 4], 24),
    ([101, 102, 103, 104], 110_355_024),
    ([], 1),
    ([1], 1),
]


@pytest.mark.parametrize('numbers, expected', testdata)
def test_run(numbers, expected):
    assert main.run(numbers) == expected
