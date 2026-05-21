import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (0, [1]),
    (1, [1, 2]),
    (2, [1, 2, 4]),
    (3, [1, 2, 4, 8]),
    (4, [1, 2, 4, 8, 16]),
    (5, [1, 2, 4, 8, 16, 32]),
    (6, [1, 2, 4, 8, 16, 32, 64]),
    (7, [1, 2, 4, 8, 16, 32, 64, 128]),
]


@pytest.mark.parametrize('n, expected', testdata)
def test_run(n, expected):
    assert main.run(n) == expected
