from src.fizzbuzz import FizzBuzz

def test_deve_retornar_fizz_quando_multiplo_de_3():
    fizzbuzz = FizzBuzz()
    assert 'fizz' == fizzbuzz.converter(3)

def test_deve_retornar_buzz_quando_multiplo_de_5():
    fizzbuzz = FizzBuzz()
    assert 'buzz' == fizzbuzz.converter(5)

def test_deve_retornar_fizzbuzz_quando_multiplo_de_3_e_5():
    fizzbuzz = FizzBuzz()
    assert 'fizzbuzz' == fizzbuzz.converter(15)

def test_deve_retornar_o_proprio_numero_quando_nao_multiplo_de_3_ou_5():
    fizzbuzz = FizzBuzz()
    assert '1' == fizzbuzz.converter(1)