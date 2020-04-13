import unittest

from phonenumbers.phonebook import PhoneBook


class PhoneBookTest(unittest.TestCase):

    def setUp(self) -> None:
        self.phoneBook = PhoneBook()

    def test_lookup_by_name(self):
        self.phoneBook.add("Bob", "12345")
        number = self.phoneBook.lookup("Bob")
        self.assertEqual("12345", number)

    def test_missing_name(self):
        with self.assertRaises(KeyError):
            self.phoneBook.lookup("missing")

    def test_empty_phonebook_is_consistent(self):
        self.assertTrue(self.phoneBook.is_consistent())

    def test_is_consistent_with_different_entries(self):
        self.phoneBook.add("Bob", "12345")
        self.phoneBook.add("Mary", "012345")
        self.assertTrue(self.phoneBook.is_consistent())

    def test_is_inconsistent_with_duplicate_entries(self):
        self.phoneBook.add("Bob", "12345")
        self.phoneBook.add("Mary", "12345")
        self.assertFalse(self.phoneBook.is_consistent())

    def test_is_inconsistent_with_duplicate_prefix(self):
        self.phoneBook.add("Bob", "12345")
        self.phoneBook.add("Mary", "123")
        self.assertFalse(self.phoneBook.is_consistent())

if __name__ == '__main__':
    unittest.main()
