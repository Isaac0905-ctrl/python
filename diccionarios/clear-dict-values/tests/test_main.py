import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (
        {'A': [0, 1], 'B': [2, 3], 'C': [4, 5]},
        {'A': [], 'B': [], 'C': []},
    ),
    (
        {'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]},
        {'C1': [], 'C2': [], 'C3': []},
    ),
]


@pytest.mark.parametrize('items, expected', testdata)
def test_run(items, expected):
    assert main.run(items) == expected
