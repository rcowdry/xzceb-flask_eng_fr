import unittest

from translator import english_to_french, french_to_english


class NullInput(unittest.TestCase):
    def test1(self):
        self.assertRaises(ValueError, english_to_french, None)
        self.assertRaises(ValueError, french_to_english, None)


class TestDouble(unittest.TestCase):
    def test1(self):
        # test when 2 is given as input the output is 4.
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        # test when -3.1 is given as input the output is -6.2.
        self.assertEqual(french_to_english("Bonjour"), "Hello")


unittest.main()
