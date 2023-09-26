import unittest

from datetime_checker import is_correct_format, is_valid_range, is_valid_date, day_in_month


class TestDateTimeChecker(unittest.TestCase):

    def test_is_correct_format(self):
        # Test cases for is_correct_format function
        self.assertTrue(is_correct_format("10", "12", "2022"))
        self.assertFalse(is_correct_format("10", "12", "abc"))

    def test_is_valid_range(self):
        # Test cases for is_valid_range function
        self.assertTrue(is_valid_range("15", "6", "2000"))
        self.assertFalse(is_valid_range("40", "6", "2000"))

    def test_day_in_month(self):
        # Test cases for day_in_month function
        self.assertEqual(day_in_month(2022, 2), 28)
        self.assertEqual(day_in_month(2024, 2), 29)

    def test_is_valid_date(self):
        # Test cases for is_valid_date function
        self.assertTrue(is_valid_date("20", "9", "2022"))
        self.assertFalse(is_valid_date("31", "4", "2022"))
