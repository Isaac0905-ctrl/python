import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ('1,2,3', '2'),
    ('1,2,3,4', '2 3'),
    ('1,2,3,4,5', '2 3 4'),
    ('1,20,300,40,5', '20 300 40'),
    ('75,5,10,100,500,1500', '5 10 100 500'),
    ('1,2', ''),
    ('1', ''),
    ('', ''),
]


@pytest.mark.parametrize('numbers, expected', testdata)
def test_run(numbers, expected):
    assert main.run(numbers) == expected
