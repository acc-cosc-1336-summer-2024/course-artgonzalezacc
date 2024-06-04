import unittest

from src.examples.b_input_proc_output.input_process_output import echo_decimal_number, echo_number, echo_string, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_echo_number(self):
        self.assertEqual(10, echo_number(10))
        self.assertEqual(100, echo_number(100))
        self.assertEqual(100.5, echo_number(100.5))

    def test_echo_decimal_number(self):
        self.assertEqual(10.5, echo_decimal_number(10.5))

    def test_echo_string(self):
        self.assertEqual("Python", echo_string("Python"))

    

