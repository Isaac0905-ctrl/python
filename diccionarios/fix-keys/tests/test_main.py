import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ({'a b   c': 1, '  de   f': 2}, {'abc': 1, 'def': 2}),
    (
        {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']},
        {'S001': ['Math', 'Science'], 'S002': ['Math', 'English']},
    ),
]


@pytest.mark.parametrize('items, expected', testdata)
def test_run(items, expected):
    assert main.run(items) == expected
