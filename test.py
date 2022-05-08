import unittest
import app

class TestInputAndOutput (unittest.TestCase):
    
    def test_upper_one(self):
        self.assertAlmostEqual("hi".upper(), "HI")
    
    def test_upper_two(self):
        self.assertAlmostEqual("hello world".upper(), "HELLO WORLD")
    
    def test_input_one(self):
        self.assertAlmostEqual(app.calculationSequence("hi"), '44444')
    
    def test_input_two(self):
        self.assertAlmostEqual(app.calculationSequence("yes"), '999337777')
        
    def test_input_three(self):
        self.assertAlmostEqual(app.calculationSequence("foo bar"), '333666666 222777')

    def test_input_four(self):
        self.assertAlmostEqual(app.calculationSequence("hello world"), '4433555555666 96667775553')
              
if __name__ == "__main__":
    unittest.main()
