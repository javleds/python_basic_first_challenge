from unittest import TestCase
from nose2.tools import params
from src.triangle import Triangle
from src.triangle_utils import get_type, get_area, get_height


class TestTriangleUtils(TestCase):
    @params(
        (Triangle(10, 10, 10), 'equilateral'),
        (Triangle(10, 20, 20), 'isosceles'),
        (Triangle(10, 20, 30), 'scalene'),
    )
    def test_get_type(self, triangle, expected):
        self.assertEqual(get_type(triangle), expected)

    @params(
        (Triangle(10, 10, 10), 43.30127018922193)
    )
    def test_get_area(self, triangle, expected):
        self.assertEqual(get_area(triangle), expected)

    @params(
        (Triangle(10, 10, 10), 8.660254037844386)
    )
    def test_get_height(self, triangle, expected):
        self.assertEqual(get_height(triangle), expected)
