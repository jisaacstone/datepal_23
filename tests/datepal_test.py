# coding: utf8
import unittest
from datepal import datepal

class TestDatePal(unittest.TestCase):

    ### POSITIVE CASES ###

    def res_equal(self, expected, date):
        self.assertEqual(expected, datepal.nearest_palindrome(date))

    def test_int(self):
        self.res_equal(1001, 1002)

    def test_str(self):
        self.res_equal("1001", "1002")

    def test_unicode_str(self):
        self.res_equal(u"1001", "1002")

    def test_identity(self):
        self.res_equal(747, 747)

    def test_neg_str(self):
        self.res_equal("0", "-1234")

    def test_neg_int(self):
        self.res_equal(0, -1234)

    ### NEGATIVE CASES ###

    def test_bad_str(self):
        with self.assertRaises(ValueError):
            datepal.nearest_palindrome("foo")

    def test_bad_type_float(self):
        with self.assertRaises(TypeError):
            datepal.nearest_palindrome(12.34)

    def test_bad_type_dict(self):
        with self.assertRaises(TypeError):
            datepal.nearest_palindrome({"fii": (1,2), "brrr": 7})

    def test_far_future(self):
        with self.assertRaises(ValueError):
            datepal.nearest_palindrome("123456789012334567890")


if __name__ == '__main__':
    unittest.main()
