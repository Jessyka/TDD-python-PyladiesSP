from src.fizzbuzz import FizzBuzz


def test_deve_retornar_fizz_quando_multiplo_de_3():
    fizzbuzz = FizzBuzz()
    assert 'fizz' == fizzbuzz.converter(3)
