from palindromo import palindromo, subPalindromo


def test_palindromo():
    assert palindromo("Anita lava la tina") == True


def test_subPalindromo():
    assert subPalindromo('AABBsopAsAposCCDD') == 'sopAsApos'
