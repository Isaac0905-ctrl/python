import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (['oveja', 'oveja', 'lobo', 'oveja'], 'Cuidado oveja 1, el lobo te va a comer'),
    (['lobo', 'oveja', 'oveja', 'oveja'], 'Cuidado oveja 3, el lobo te va a comer'),
    (['lobo', 'oveja'], 'Cuidado oveja 1, el lobo te va a comer'),
    (['lobo', 'oveja', 'oveja'], 'Cuidado oveja 2, el lobo te va a comer'),
    (['oveja', 'oveja', 'oveja', 'lobo'], 'Oye lobo no te quiero ver más por aquí'),
]


@pytest.mark.parametrize('farm, expected', testdata)
def test_run(farm, expected):
    assert main.run(farm) == expected
