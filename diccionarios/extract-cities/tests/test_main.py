import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (
        'Tokyo:38_140_000;Delhi:26_454_000;Shanghai:24_484_000;Mumbai:21_357_000',
        {'Tokyo': 38140000, 'Delhi': 26454000, 'Shanghai': 24484000, 'Mumbai': 21357000},
    ),
    (
        'Adeje:49_270;La Orotava:42_434;Los Silos:4644;Santa Úrsula:15_361;Tegueste:11_359',
        {
            'Adeje': 49270,
            'La Orotava': 42434,
            'Los Silos': 4644,
            'Santa Úrsula': 15361,
            'Tegueste': 11359,
        },
    ),
    ('Agaete:5633;Gáldar:24_567;Telde:102_472', {'Agaete': 5633, 'Gáldar': 24567, 'Telde': 102472}),
    (
        'Tanzania:52_482_726;Kenia:46_790_758;Camerún:24_360_803;Zambia:752_618',
        {'Tanzania': 52482726, 'Kenia': 46790758, 'Camerún': 24360803, 'Zambia': 752_618},
    ),
]


@pytest.mark.parametrize('cinfo, expected', testdata)
def test_run(cinfo, expected):
    assert main.run(cinfo) == expected
