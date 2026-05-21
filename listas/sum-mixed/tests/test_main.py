import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ([1, '2', 3, '4', 5], 15),
    (['0', '-1', '-2', '-3', '-4', '-5'], -15),
    ([100, 90, 80, 70, '60', '50', '40', '30', '20', '10'], 550),
]


@pytest.mark.parametrize('items, expected', testdata)
def test_run(items, expected):
    assert main.run(items) == expected
