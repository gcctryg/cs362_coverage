import unittest
import leapYear

class testCaseLeapYear(unittest.TestCase):
    def testLeapYear(self):
        self.assertTrue(leapYear.checkLeapYear(2003))
        self.assertFalse(leapYear.checkLeapYear(2003))


if __name__ == '__main__':
    unittest.main()