import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ([3, [6, 9], 12], [3, 6, 9, 12]),
    (
        [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]],
        [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],
    ),
    (['a', ['b', 'c'], 'd'], ['a', 'b', 'c', 'd']),
    ([[1], [2], [3], [4]], [1, 2, 3, 4]),
]


@pytest.mark.parametrize('items, expected', testdata)
def test_run(items, expected):
    assert main.run(items) == expected
