from palindromo import palindromo, subPalindromo
import pytest


def test_palindromo():
    assert palindromo("Anita lava la tina") == True


def test_subPalindromo():
    assert subPalindromo('AABBsopAsAposCCDD') == 'sopAsApos'


@pytest.mark.parametrize(
    "input_a, expected",
    [
        ('Anita lava la tina', True),
        ('AABBsopAsAposCCDD', False),
        ('123456 6 54321', True)

    ]
)
def test_palindromo_multi(input_a, expected):
    assert palindromo(input_a) == expected
