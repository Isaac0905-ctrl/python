import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (1, (1, 1)),
    (2, (9, 9)),
    (3, (36, 36)),
    (4, (100, 100)),
    (5, (225, 225)),
]


@pytest.mark.parametrize('n, expected', testdata)
def test_run(n, expected):
    assert main.run(n) == expected
