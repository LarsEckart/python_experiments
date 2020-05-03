def test_a_typical_common_year():
    actual = Year(2019)
    assert actual.is_leap_year() is False


def test_a_typical_leap_year():
    actual = Year(1996)
    assert actual.is_leap_year() is True


def test_an_atypical_common_year():
    actual = Year(1900)
    assert actual.is_leap_year() is False


def test_an_atypical_leap_year():
    actual = Year(2000)
    assert actual.is_leap_year() is True


class Year:
    def __init__(self, year):
        self._year = year

    def is_leap_year(self):

        if self.is_divisible_by(4) and self.is_divisible_by(400):
            return True

        if self.is_divisible_by(4) and not self.is_divisible_by(100):
            return True

        return False

    def is_divisible_by(self, number):
        return self._year % number == 0
