import unittest
import UnitTest.main as main


# define test class *required*
class testTESTING(unittest.TestCase):

    def TestPositiveNumber(self):
        result = main.DivideByTwo(20)
        self.assertEqual(result,10)

    def TestNegativeNumber(self):
        result = main.DivideByTwo(-20)
        self.assertEqual(result,-10)


# create test suite
TestSuite = unittest.TestSuite()

# add tests to suite
TestSuite.addTest(testTESTING("TestPositiveNumber"))
TestSuite.addTest(testTESTING("TestNegativeNumber"))


# create runner
runner = unittest.TextTestRunner()

# execute tests
runner.run(TestSuite)
