class FizzBuzz:
    def __init__(self, num):
        self._num = num

    def value(self):
        if self._num % 3 == 0 and self._num % 5 == 0:
            return 'FizzBuzz'

        if self._num % 3 == 0:
            return 'Fizz'

        if self._num % 5 == 0:
            return 'Buzz'

        return str(self._num)
