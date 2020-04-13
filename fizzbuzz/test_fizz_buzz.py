from fizzbuzz import FizzBuzz


def test_returns_1_for_1():
    f = FizzBuzz(1)
    assert f.value() == '1'


def test_returns_2_for_2():
    f = FizzBuzz(2)
    assert f.value() == '2'


def test_returns_fizz_for_3():
    f = FizzBuzz(3)
    assert f.value() == 'Fizz'


def test_returns_fizz_for_6():
    f = FizzBuzz(6)
    assert f.value() == 'Fizz'


def test_returns_buzz_for_5():
    f = FizzBuzz(5)
    assert f.value() == 'Buzz'


def test_returns_buzz_for_10():
    f = FizzBuzz(10)
    assert f.value() == 'Buzz'


def test_returns_fizzbuzz_for_15():
    f = FizzBuzz(15)
    assert f.value() == 'FizzBuzz'


def test_returns_fizzbuzz_for_30():
    f = FizzBuzz(30)
    assert f.value() == 'FizzBuzz'


def test_1_to_100():
    print("\n")
    for i in range(1, 101):
        print(f"{i}: {FizzBuzz(i).value()}")
