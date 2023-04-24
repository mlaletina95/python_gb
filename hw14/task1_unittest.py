import unittest
from task1 import delete_non_alphabet_and_spaces

class TestDeleteAlphabetAndSpaces(unittest.TestCase):
    def test_string_unchanged(self):
        self.assertEqual(delete_non_alphabet_and_spaces('hello world b a'), 'hello world b a')

    def test_registry(self):
        self.assertEqual(delete_non_alphabet_and_spaces('HELLO WORLD B A'), 'hello world b a')

    def test_punctuation(self):
        self.assertEqual(delete_non_alphabet_and_spaces('hello, world: b, a!'), 'hello world b a')

    def test_non_latin(self):
        self.assertEqual(delete_non_alphabet_and_spaces('hello world b aцш!'), 'hello world b a')

    def test_mixed(self):
        self.assertEqual(delete_non_alphabet_and_spaces('HELLO, world: b, a,цш!'), 'hello world b a')


if __name__ == '__main__':
    unittest.main("-vv")