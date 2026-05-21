import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (['U', 'V', 'W', 'X', 'Y'], ['V', 'X']),
    ([2, 1, 2, 1, 2, 1], [1, 1, 1]),
    ([10, 20], [20]),
    (['a', 'b', 'a', 'b', 'a'], ['b', 'b']),
    ([1, 10, 2, 20, 3, 30, 4, 40], [10, 20, 30, 40]),
]


@pytest.mark.parametrize('items, expected', testdata)
def test_run(items, expected):
    assert main.run(items) == expected
