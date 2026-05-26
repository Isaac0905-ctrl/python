import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (35231, [1, 3, 2, 5, 3]),
    (4287690, [0, 9, 6, 7, 8, 2, 4]),
    (0, [0]),
    (1, [1]),
]


@pytest.mark.parametrize('number, expected', testdata)
def test_run(number, expected):
    assert main.run(number) == expected
