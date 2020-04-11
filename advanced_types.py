import unittest


class CorePython(unittest.TestCase):

    def test_string_to_int(self):
        self.assertEqual(3, int("3"))

    def test_string_index_access(self):
        self.assertEqual("L", "Lars"[0])
        self.assertEqual('L', 'Lars'[0])

    def test_string_capitalization(self):
        self.assertEqual("Lars", "lars".capitalize())

    def test_string_uppercase(self):
        self.assertEqual("LARS", "lars".upper())

    def test_lists(self):
        self.assertEqual(0, len([]))
        myList = [1, 2]
        myList.append(3)
        self.assertEqual([1, 2, 3], myList)
        self.assertEqual(["1", "2", "3"], list("123"))

    def test_dicts(self):
        d = {'bob': '13-456-890'}
        self.assertEqual('13-456-890', d['bob'])
        d['oskar'] = '987-6543-210'
        self.assertEqual(2, len(d))
        self.assertEqual(0, len({}))

    def for_loops(self):
        cities = ['Tallinn', 'Tartu', 'Pärnu']
        for city in cities:
            self.assertTrue(city)

    def test_iterating_over_dict_returns_keys(self):
        d = {'Lars': 34, 'Oskar': 3}
        for name in d:
            self.assertTrue(name == 'Lars' or name == 'Oskar')

    def test_iterating_over_dict_can_access_key_and_value(self):
        d = {'Lars': 34}
        for name in d:
            r = name + str(d[name])
            self.assertEqual('Lars34', r)




if __name__ == '__main__':
    unittest.main()
