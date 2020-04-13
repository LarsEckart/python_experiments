import pytest


def test_lookup_by_name():
    phone_book = PhoneBook()
    phone_book.add("Bob", "12345")
    assert "12345" == phone_book.lookup("Bob")


def test_phonebook_contains_all_names():
    phone_book = PhoneBook()
    phone_book.add("Bob", "12345")
    assert phone_book.names() == {"Bob"}
    assert "Bob" in phone_book.names()


def test_missing_name_raises_error():
    phone_book = PhoneBook()
    with pytest.raises(KeyError):
        phone_book.lookup("Bob")


class PhoneBook:
    def __init__(self):
        self._numbers = {}

    def add(self, name, number):
        self._numbers[name] = number

    def lookup(self, name):
        return self._numbers[name]

    def names(self):
        return set(self._numbers.keys())
