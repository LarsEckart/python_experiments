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

    def test_tuples(self):
        t = ("Hello", 3.14, 42)
        self.assertEqual("Hello", t[0])
        self.assertEqual(42, t[2])

    def test_tuple_concat(self):
        t = ("Hello", "world")
        t = t + ("how", "are", "you")
        self.assertEqual(("Hello", "world", "how", "are", "you"), t)

    def test_tuple_of_one(self):
        t = (42,)

    def test_string_joining(self):
        colors = ';'.join(["red", "green", "blue"])
        self.assertEqual("red;green;blue", colors)

    def test_string_partition(self):
        t = "unforgetable".partition('forget')
        self.assertEqual(("un", "forget", "able"), t)

    def test_string_destructuring(self):
        departure, separator, arrival = "London:Edinburgh".partition(":")
        self.assertEqual("London", departure)
        self.assertEqual(":", separator)
        self.assertEqual("Edinburgh", arrival)

    def test_string_format(self):
        s = "{1}, {0}".format("Lars", "Eckart")
        self.assertEqual("Eckart, Lars", s)

    def test_fstrings(self):
        value = 42 * 1
        self.assertEqual("The value is 42", f'The value is {value}')

    def test_ranges_with_one_argument_starts_at_zero_and_deos_not_include_parameter(self):
        r = range(5)
        self.assertEqual([0, 1, 2, 3, 4], list(r))

    def test_range_with_step_count(self):
        r = range(0, 10, 2)
        self.assertEqual([0, 2, 4, 6, 8], list(r))

    def test_use_enumerate_to_get_tuple_of_index_and_item(self):
        t = [2, 4, 6]
        for i, v in enumerate(t):
            t[i] = v * i
        self.assertEqual([0, 4, 12], t)

    def test_list_negative_indices_give_elements_from_the_end(self):
        l = range(11)
        self.assertEqual(10, l[-1])

    def test_slicing(self):
        names = ["Lars", "Florian", "Christoph", "Rutger"]
        self.assertEqual(["Florian", "Christoph"], names[1:3])
        self.assertEqual(["Christoph", "Rutger"], names[2:])
        self.assertEqual(["Lars"], names[:1])

    def test_slice_copying(self):
        s = [2, 4, 6, 8]
        t = s[:]
        self.assertEqual(t, s)
        self.assertFalse(t is s)

    def test_other_copy_options(self):
        s = [2, 4, 6, 8]
        t = s.copy()
        self.assertEqual(t, s)
        self.assertFalse(t is s)

        t = list(s)
        self.assertEqual(t, s)
        self.assertFalse(t is s)

    def test_list_multiplication(self):
        s = [0] * 10
        self.assertEqual([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], s)

    def test_list_index(self):
        words = "lars on tubli poiss".split()
        i = words.index("tubli")
        self.assertEqual(2, i)

    def test_count_occurrences(self):
        s = "a fox is not a dog"
        self.assertEqual(2, s.count("a"))

    def test_membership(self):
        s = "lars on tubli poiss"
        self.assertTrue('lars' in s)
        self.assertTrue('Lars' not in s)

    def test_dicts_more(self):
        d = {"hello": "world", "lars": "eckart"}
        self.assertTrue("lars" in d.keys())
        self.assertTrue("world" in d.values())
        self.assertTrue(("hello", "world") in d.items())

    def test_sets(self):
        set = {1, 2, 3, 4, 5, 1, 2}
        short = {1, 2, 3, 4, 5}
        self.assertEqual(set, short)


if __name__ == '__main__':
    unittest.main()
