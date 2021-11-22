#!/usr/bin/python3
# Test case for multiplying a list elements with '2'
import unittest

from code import mul_by_2

class TestSum(unittest.TestCase):
    def test_list_int(self):

        data = [10,20,30,40,50]
        result = mul_by_2(data)
        self.assertEqual(result, [20,40,60,80,100])

if __name__ == '__main__':
    unittest.main()
