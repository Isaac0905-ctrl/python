import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ([1, 2, 3, 4], 2, 9),
    ([10, 20, 30, 40, 50], 4, 6_250_000),
    ([1, 2, 3], 3, -1),
]


@pytest.mark.parametrize('values, n, expected', testdata)
def test_run(values, n, expected):
    assert main.run(values, n) == expected
