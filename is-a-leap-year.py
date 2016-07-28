import unittest

def is_leap_year(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    # Not divisible by 100
    if year % 4 == 0:
        return True
    return False

class TestLeapYear(unittest.TestCase):

    def test_is_leap_year(self):
        self.assertTrue(is_leap_year(2000))
        self.assertTrue(is_leap_year(2400))
        self.assertFalse(is_leap_year(1800))
        self.assertFalse(is_leap_year(1900))
        self.assertFalse(is_leap_year(2100))
        self.assertFalse(is_leap_year(2200))
        self.assertFalse(is_leap_year(2300))
        self.assertFalse(is_leap_year(2500))
