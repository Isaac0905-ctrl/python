import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (
        ('Guido van Rossum', 'guido van rossum', 'Guido Van rossum', 'Guido Van Rossum'),
        """¿Su nombre?
Error. Debe escribirlo correctamente
¿Su nombre?
Error. Debe escribirlo correctamente
¿Su nombre?
Error. Debe escribirlo correctamente
¿Su nombre?""",
    ),
    (
        (
            'ada lovelace',
            'Ada lovelace',
            'ada Lovelace',
            'ADA LOVELACE',
            'ADA lovelace',
            'ada LOVELACE',
            'Ada Lovelace',
        ),
        """¿Su nombre?
Error. Debe escribirlo correctamente
¿Su nombre?
Error. Debe escribirlo correctamente
¿Su nombre?
Error. Debe escribirlo correctamente
¿Su nombre?
Error. Debe escribirlo correctamente
¿Su nombre?
Error. Debe escribirlo correctamente
¿Su nombre?
Error. Debe escribirlo correctamente
¿Su nombre?""",
    ),
]


@pytest.mark.parametrize('inputs, expected', testdata)
def test_run(inputs, expected, monkeypatch, capsys):
    def gen_input():
        yield from inputs

    test_inputs = gen_input()

    def monkey_input(msg: str) -> str:
        print(msg.strip())
        return next(test_inputs)

    monkeypatch.setattr('builtins.input', monkey_input)
    main.run()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected
