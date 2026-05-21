import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ([4, 4, 4], True),
    ([4, 3, 4], False),
    ([1, 1, 1, 1, 1, 1], True),
    ([1, 1, 1, 1, 2], False),
    (['a', 'b', 'c'], False),
    (['', '', ''], True),
]


@pytest.mark.parametrize('items, expected', testdata)
def test_run(items, expected):
    assert main.run(items) == expected
