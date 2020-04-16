class StringCalculator:
    def sum(param):
        if not param:
            return 0
        return int(param)


def test_empty_string_returns_zero():
    string_calculator = StringCalculator()
    actual = string_calculator.sum('')
    assert actual == 0


def test_same_number_for_single_number_input():
    string_calculator = StringCalculator()
    actual = string_calculator.sum('42')
    assert actual == 42
