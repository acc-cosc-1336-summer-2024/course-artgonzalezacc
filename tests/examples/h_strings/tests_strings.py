import unittest

from src.examples.h_strings.strings import test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_access_characters_in_a_string(self):
        lang = "Python"

        self.assertEqual('P', lang[0])
        self.assertEqual('y', lang[1])
        self.assertEqual('t', lang[2])
        self.assertEqual('h', lang[3])
        self.assertEqual('o', lang[4])
        self.assertEqual('n', lang[5])

    def test_len_of_string_function(self):
        lang = "Python"

        self.assertEqual(6, len(lang))

    def test_string_w_in(self):
        lang = "Python"
        result = 'th' in lang # will be True or False

        self.assertEqual(True, result)

    def test_string_w_not_in(self):
        lang = "Python"

        self.assertEqual(True, 'Th' not in lang)

    def test_string_is_digit(self):
        num = "1234"

        self.assertEqual(True, num.isdigit())

    def test_string_is_lower(self):
        lang = "python"

        self.assertEqual(True, lang.islower())

    def test_string_is_alpha(self):
        lang = "abcdefg"

        self.assertEqual(True, lang.isalpha())

    def test_string_to_lower(self):
        str = "PYTHON"
        str_lower =  str.lower()

        self.assertEqual(True, "python" == str_lower)

    def test_string_rstrip(self):
        str = "Python     "
        str_stripped = str.rstrip()

        self.assertEqual(True, "Python" == str_stripped)

    def test_find_in_string(self):
        str = "Four score and seven years ago"
        position = str.find("seven")

        self.assertEqual(True, position != -1)

    def test_replace_in_string(self):
        str = "Four score and seven years ago"
        new_str = str.replace('years', 'days')

        self.assertEqual(True, 'Four score and seven days ago' == new_str)

