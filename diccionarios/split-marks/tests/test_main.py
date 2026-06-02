import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (
        {'Alex': 5, 'Adriana': 9, 'Mauro': 3, 'Maika': 4},
        ({'ALEX': 5, 'ADRIANA': 9}, {'mauro': 3, 'maika': 4}),
    ),
    (
        {'Ana': 4, 'Domingo': 7, 'Eva': 5, 'Álvaro': 3, 'Juan': 8, 'Belén': 1},
        ({'DOMINGO': 7, 'EVA': 5, 'JUAN': 8}, {'ana': 4, 'álvaro': 3, 'belén': 1}),
    ),
]


@pytest.mark.parametrize('marks, expected', testdata)
def test_run(marks, expected):
    assert main.run(marks) == expected
