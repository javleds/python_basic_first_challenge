from unittest import TestCase
from nose2.tools import params
from src.unit_converter import kilometers_to_miles, miles_to_kilometers


class TestUnitConverter(TestCase):
    @params(
        (1.609344, 1),
        (16.09344, 10),
        (160.9344, 100),
    )
    def test_kilometers_to_miles(self, kilometers, expected):
        self.assertEqual(kilometers_to_miles(kilometers), expected)

    @params(
        (1, 1.609344),
        (10, 16.09344),
        (100, 160.9344),
    )
    def test_miles_to_kilometers(self, miles, expected):
        self.assertEqual(miles_to_kilometers(miles), expected)
