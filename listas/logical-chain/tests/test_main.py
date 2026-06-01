import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ([False, False], 'and', False),
    ([False, True], 'and', False),
    ([True, False], 'and', False),
    ([True, True], 'and', True),
    ([False, False], 'or', False),
    ([False, True], 'or', True),
    ([True, False], 'or', True),
    ([True, True], 'or', True),
    ([True, True, False], 'and', False),
    ([True, True, False], 'or', True),
    ([True, True, True], 'and', True),
    ([True, True, True], 'or', True),
    ([False, False, False], 'and', False),
    ([False, False, False], 'or', False),
    ([True, False, False, True], 'or', True),
    ([False, True, False, True], 'and', False),
]


@pytest.mark.parametrize('values, oper, expected', testdata)
def test_run(values, oper, expected):
    assert main.run(values, oper) == expected
