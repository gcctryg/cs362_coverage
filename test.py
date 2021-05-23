import unittest
import leapYear

class testCaseLeapYear(unittest.TestCase):
    def testLeapYear(self):
        #result = calc.add(10,5)
       # self.assertEqual(result, 15)
        self.assertTrue(leapYear.checkLeapYear(2003))
        self.assertFalse(leapYear.checkLeapYear(2003))


if __name__ == '__main__':
    unittest.main()