import unittest

from datetime_checker import check_date

class TestCheckDateFunction(unittest.TestCase):
    def test_with_null_year(self):
        self.assertEqual(check_date(1,1,"asf"), {'message': f"Input data for Year is incorrect format!", 'status': False})



