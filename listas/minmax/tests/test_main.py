import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ([4, 2, 8, 11, 23, 8, 9], (2, 23)),
    ([4, 6, 2, 1, 9, 63, -134, 566], (-134, 566)),
    ([-52, 56, 30, 29, -54, 0, -110], (-110, 56)),
    ([42, 54, 65, 87, 0], (0, 87)),
    ([5], (5, 5)),
]


@pytest.mark.parametrize('values, expected', testdata)
def test_run(values, expected):
    assert main.run(values) == expected
