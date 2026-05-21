import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ([[4, 6, 1], [2, 9, 3], [1, 7, 7]], 20),
    ([[1, 1], [1, 1]], 2),
    ([[1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 10, 11], [4, 2, 1, 8]], 24),
    ([[5, 1, 9], [3, 4, 2], [8, 7, 6]], 15),
    ([[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]], None),
]


@pytest.mark.parametrize('matrix, expected', testdata)
def test_run(matrix, expected):
    assert main.run(matrix) == expected
