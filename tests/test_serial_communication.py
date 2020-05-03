#!/usr/bin/env python3
"""
File:          serial_communicator.py
Author:        Piyush Shah
Last Modified: Piyush on 5/2
"""

import sys

from src.serial_communication import SerialComm

# Attempt to use back-ported unittest2 for Python 2.6 and earlier
# However, it is strongly recommended to use Python 2.7 or 3.<latest>

import unittest

class SerialCommTest(unittest.TestCase):
    def setUp(self):
        self.sercom = SerialComm()

    def test_handel_feedback(self):
        value = self.sercom.handel_feedback("123")
        self.assertEqual(value, None, FAILURE)

    # def test_add(self):
    #     value = self.calc.add(NUMBER_1, NUMBER_2)
    #     self.assertEqual(value, 5.0, FAILURE)
    #     self.assertEqual(value, self.calc.last_answer, FAILURE)

    # def test_subtract(self):
    #     value = self.calc.subtract(NUMBER_1, NUMBER_2)
    #     self.assertEqual(value, 1.0, FAILURE)
    #     self.assertEqual(value, self.calc.last_answer, FAILURE)

    # def test_subtract_negative(self):
    #     value = self.calc.subtract(NUMBER_2, NUMBER_1)
    #     self.assertEqual(value, -1.0, FAILURE)
    #     self.assertEqual(value, self.calc.last_answer, FAILURE)

    # def test_multiply(self):
    #     value = self.calc.multiply(NUMBER_1, NUMBER_2)
    #     self.assertEqual(value, 6.0, FAILURE)
    #     self.assertEqual(value, self.calc.last_answer, FAILURE)

    # def test_divide(self):
    #     value = self.calc.divide(NUMBER_1, NUMBER_2)
    #     self.assertEqual(value, 1.5, FAILURE)
    #     self.assertEqual(value, self.calc.last_answer, FAILURE)

    # def test_divide_by_zero(self):
    #     self.assertRaises(ZeroDivisionError, self.calc.divide, NUMBER_1, 0)

    # def test_max_greater(self):
    #     value = self.calc.maximum(NUMBER_1, NUMBER_2)
    #     self.assertEqual(value, NUMBER_1, FAILURE)
    #     self.assertEqual(value, self.calc.last_answer, FAILURE)

    # def test_max_less(self):
    #     value = self.calc.maximum(NUMBER_2, NUMBER_1)
    #     self.assertEqual(value, NUMBER_1, FAILURE)
    #     self.assertEqual(value, self.calc.last_answer, FAILURE)

    # def test_max_equal(self):
    #     value = self.calc.maximum(NUMBER_1, NUMBER_1)
    #     self.assertEqual(value, NUMBER_1, FAILURE)
    #     self.assertEqual(value, self.calc.last_answer, FAILURE)

    # def test_min_greater(self):
    #     value = self.calc.minimum(NUMBER_1, NUMBER_2)
    #     self.assertEqual(value, NUMBER_2, FAILURE)
    #     self.assertEqual(value, self.calc.last_answer, FAILURE)

    # def test_min_less(self):
    #     value = self.calc.minimum(NUMBER_2, NUMBER_1)
    #     self.assertEqual(value, NUMBER_2, FAILURE)
    #     self.assertEqual(value, self.calc.last_answer, FAILURE)

    # def test_min_equal(self):
    #     value = self.calc.minimum(NUMBER_2, NUMBER_2)
    #     self.assertEqual(value, NUMBER_2, FAILURE)
    #     self.assertEqual(value, self.calc.last_answer, FAILURE)


if __name__ == '__main__':
    unittest.main()