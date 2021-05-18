from unittest import TestCase
from nose2.tools import params
from src.number_utils import is_float


class TestNumberUtils(TestCase):
    @params(
        ('', False),
        ('some', False),
        ('1', True),
        ('10.5', True),
        ('10.5.5', False),
    )
    def test_is_float(self, value, expected):
        self.assertEqual(is_float(value), expected)
