import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ([2, 2, 3], [5, 4, 1], 8),
    ([3, 4, 2], [9, 1, 6], 30),
    ([1, 1, 1], [1, 1, 1], 0),
]


@pytest.mark.parametrize('cuboid1, cuboid2, expected', testdata)
def test_run(cuboid1, cuboid2, expected):
    assert main.run(cuboid1, cuboid2) == expected
