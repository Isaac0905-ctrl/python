import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (1, 10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    (2, 5, [2, 4, 6, 8, 10]),
    (3, 8, [3, 6, 9, 12, 15, 18, 21, 24]),
]


@pytest.mark.parametrize('x, n, expected', testdata)
def test_run(x, n, expected):
    assert main.run(x, n) == expected
