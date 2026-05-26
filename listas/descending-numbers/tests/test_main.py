import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (5, [5, 4, 3, 2, 1]),
    (10, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),
    (1, [1]),
    (0, []),
]


@pytest.mark.parametrize('n, expected', testdata)
def test_run(n, expected):
    assert main.run(n) == expected
