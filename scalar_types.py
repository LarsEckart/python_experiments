import unittest


class CorePython(unittest.TestCase):

    def test_float_to_int_by_calling_constructor_which_rounds_towards_zero(self):
        self.assertEqual(3, int(3.5))
        self.assertEqual(-3, int(-3.5))

    def test_string_to_int(self):
        self.assertEqual(3, int("3"))

    def test_can_specify_ints_with_binary_by_prefixing_0b(self):
        self.assertEqual(0b10, 2)

    def test_None(self):
        a = None
        self.assertIsNone(a)

    def test_boolean_truthy(self):
        self.assertTrue(True)
        self.assertTrue(bool(42))
        self.assertTrue([1, 2, 3])
        self.assertTrue("hello")
        self.assertTrue("True")
        self.assertTrue("False")

    def test_boolean_falsy(self):
        self.assertFalse(False)
        self.assertFalse(bool(0))
        self.assertFalse([])
        self.assertFalse("")

    def test_relational_operators(self):
        self.assertTrue("True" == "True")
        self.assertTrue("True" != "False")
        self.assertTrue(3 < 5)
        self.assertTrue(7 > 5)

    def test_if_statements(self):
        if True:
            self.assertTrue(True)
        if False:
            self.assertTrue(False)
        if bool("hello"):
            self.assertTrue(True)
        if "hello":
            self.assertTrue(True)

    def test_if_else_clause(self):
        x = 5
        if x > 7:
            self.assertTrue(False)
        else:
            self.assertTrue(True)

    def test_if_else_if_clause(self):
        x = 5
        if x > 7:
            self.assertTrue(False)
        elif x < 10:
            self.assertTrue(True)
        else:
            self.assertTrue(True)

    def test_while_loop(self):
        i = 5
        while i > 0:
            i -= 1

        self.assertEqual(0, i)


if __name__ == '__main__':
    unittest.main()
