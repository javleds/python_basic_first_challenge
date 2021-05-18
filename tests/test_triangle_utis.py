from unittest import TestCase
from nose2.tools import params
from src.triangle import Triangle
from src.triangle_utils import get_type


class TestTriangleUtils(TestCase):
    @params(
        (Triangle(10, 10, 10), 'equilateral'),
        (Triangle(10, 20, 20), 'isosceles'),
        (Triangle(10, 20, 30), 'scalene'),
    )
    def test_get_type(self, triangle, expected):
        self.assertEqual(get_type(triangle), expected)
