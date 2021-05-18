from unittest import TestCase
from nose2.tools import params
from src.string_utils import is_palindrome


class TestStringUtils(TestCase):
    @params(
        ('Anita lava la tina', True),
        ('Nice try', False)
    )
    def test_is_palindrome(self, phrase, expected):
        self.assertEqual(is_palindrome(phrase), expected)
