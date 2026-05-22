import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ('17:15', 240, '21:15'),
    ('8:05', 265, '12:30'),
    ('22:55', 315, '4:10'),
]


@pytest.mark.parametrize('time, offset, expected', testdata)
def test_run(time, offset, expected):
    assert main.run(time, offset) == expected
