import unittest  # Import the unittest module
import calc  # Import the calc module (assuming it contains the add function)

# Define a test case class that inherits from unittest.TestCase
class Test_Calc(unittest.TestCase):
   
    # Define a test method named test_add
    def test_add(self): #self is a convention
        # Call the add function from the calc module with arguments 10 and 5
        result = calc.add(10, 5)
        # Use assertEqual to verify that the result equals 15
        self.assertEqual(result, 15) #result is a output value, 15 is a expected value

# The following code runs the tests when the script is executed directly
if __name__ == '__main__': #instead of this code we can use CLI
    unittest.main()
