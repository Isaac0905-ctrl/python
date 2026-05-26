import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ([1, 2, 3, 4], 3, [[1, 2, 3], [2, 3, 4]]),
    ([1, 2, 3, 4], 2, [[1, 2], [2, 3], [3, 4]]),
    ([1, 2, 3, 4], 1, [[1], [2], [3], [4]]),
    ([], 1, []),
]


@pytest.mark.parametrize('values, size, expected', testdata)
def test_run(values, size, expected):
    assert main.run(values, size) == expected
