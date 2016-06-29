import unittest
from adder import adder

class Test(unittest.TestCase):

    def test_adder_errors(self):
        self.assertRaises(TypeError, adder, "123", "456")
        self.assertRaises(TypeError, adder, "123", 456)
        self.assertRaises(TypeError, adder, 123, "456")
        self.assertRaises(TypeError, adder, 1.23, 456)
    
    def test_adder_successes(self):
        self.assertTrue(adder(1, 2) == 3, "1 + 2 is not 3")
        
if __name__ == "__main__":
    unittest.main()
