import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (0, '0'),
    (1, '1'),
    (11, '1011'),
    (42, '101010'),
    (56, '111000'),
    (99, '1100011'),
    (120, '1111000'),
    (237, '11101101'),
]


@pytest.mark.parametrize('n, expected', testdata)
def test_run(n, expected):
    assert main.run(n) == expected
