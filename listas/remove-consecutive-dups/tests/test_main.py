import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]),
    (['a', 'b', 'b', 'b', 'c', 'b'], ['a', 'b', 'c', 'b']),
    ([1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0], [1, 0, 1, 0, 1, 0]),
    (['Z', 'W', 'W', 'W', 'X', 'Y', 'Y', 'W'], ['Z', 'W', 'X', 'Y', 'W']),
    ([4, 2, 3, 1, 7, 4], [4, 2, 3, 1, 7, 4]),
]


@pytest.mark.parametrize('items, expected', testdata)
def test_run(items, expected):
    assert main.run(items) == expected
