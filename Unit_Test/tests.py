import unittest
import Unit_Test.main as main


# define test class *required*
class TestMain(unittest.TestCase):

    def TestPositiveNumber(self):
        result = main.DivideByTwo(20)
        self.assertEqual(result,10)

    def TestNegativeNumber(self):
        result = main.DivideByTwo(-20)
        self.assertEqual(result,-10)


# create test suite
TestSuite = unittest.TestSuite()

# add tests to suite
TestSuite.addTest(TestMain("TestPositiveNumber"))
TestSuite.addTest(TestMain("TestNegativeNumber"))


# create runner
runner = unittest.TextTestRunner()

# execute tests
runner.run(TestSuite)
