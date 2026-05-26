import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ([1, 2, 3, 4], [1, 1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([1, 11], [1, 2, 10], [1, 2, 10, 11]),
    ([2, 4, 4, 5, 9], [1, 3, 6, 6, 10, 10], [1, 2, 3, 4, 5, 6, 9, 10]),
    ([20, 30], [40, 50], [20, 30, 40, 50]),
    ([], [], []),
]


@pytest.mark.parametrize('values1, values2, expected', testdata)
def test_run(values1, values2, expected):
    assert main.run(values1, values2) == expected
