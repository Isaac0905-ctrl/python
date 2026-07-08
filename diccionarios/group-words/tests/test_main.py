import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (
        ['azul', 'blanco', 'negro', 'amarillo', 'beige', 'naranja'],
        {'a': ['azul', 'amarillo'], 'b': ['blanco', 'beige'], 'n': ['negro', 'naranja']},
    ),
    (
        [
            'mesa',
            'móvil',
            'barco',
            'coche',
            'avión',
            'bandeja',
            'casa',
            'monitor',
            'carretera',
            'arco',
        ],
        {
            'm': ['mesa', 'móvil', 'monitor'],
            'b': ['barco', 'bandeja'],
            'c': ['coche', 'casa', 'carretera'],
            'a': ['avión', 'arco'],
        },
    ),
]


@pytest.mark.parametrize('words, expected', testdata)
def test_run(words, expected):
    assert main.run(words) == expected
