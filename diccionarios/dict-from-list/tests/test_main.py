import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (
        [['Item1', 'A', 'B'], ['Item2', 'C', 'D'], ['Item3', 'E', 'F']],
        {'Item1': ['A', 'B'], 'Item2': ['C', 'D'], 'Item3': ['E', 'F']},
    ),
    (
        [
            ['Episode IV - A New Hope', 'May 25', 1977, 'George Lucas'],
            ['Episode V - The Empire Strikes Back', 'May 21', 1980],
            ['Episode VI - Return of the Jedi', 'May 25', 1983],
        ],
        {
            'Episode IV - A New Hope': ['May 25', 1977, 'George Lucas'],
            'Episode V - The Empire Strikes Back': ['May 21', 1980],
            'Episode VI - Return of the Jedi': ['May 25', 1983],
        },
    ),
]


@pytest.mark.parametrize('items, expected', testdata)
def test_run(items, expected):
    assert main.run(items) == expected
