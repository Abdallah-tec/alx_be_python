import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(10,5), 15)
        self.assertEqual(self.calc.add(-2,2), 0)
    
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10,5), 5)
        self.assertEqual(self.calc.subtract(-2,2), -4)
    
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(9,9), 81)
    
    def test_division(self):
        self.assertEqual(self.calc.divide(10,10), 1)
        self.assertEqual(self.calc.divide(10,0), None)


if __name__ == "__main__":
    unittest.main()
