# ----------------------------------------------------
# -- Advanced Lessons => Unit Testing With Unittest --
# ----------------------------------------------------
# Test Runner
# - The Module That Run The Unit Testing (unittest, pytest)
# ----------------------------------------------------
# Test Case
# - Smallest Unit Of Testing 
# - It Use Asserts Methods To Chech For Actions And Responses 
# Test Suite
# - Collection Of Multiple Tests Or Test Cases
# Test Report
# - A Full Report Contains The Failure Or Succeed
# ----------------------------------------------------
# unittest
# - Add Tests Into Classes As Methods
# - Use A Series Of Special Assertion Methods 
# https://docs.python.org/3/library/unittest.html
# ----------------------------------------------------

import unittest

# assert 3 * 8 == 25, "Should Be 24"

# def test_case_one():

#     assert 10 * 10 == 100, "Should Be 100"

# def test_case_two():

#     assert 10 * 2 == 20, "Should Be 20"

# if __name__ == "__main__":

#     test_case_one()
#     test_case_two()

#     print("All Test Passed")

class MyTestCase(unittest.TestCase):

    def test_one(self):

        self.assertTrue(100 > 56, "Should Be True")

    def test_two(self):

        self.assertEqual(20 + 80, 100, "Should Be 100")

    def test_three(self):

        self.assertGreater(100, 80, "Should Be True")



if __name__ == "__main__":

    unittest.main()