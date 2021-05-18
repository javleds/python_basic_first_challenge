from unittest import TestCase
from nose2.tools import params
from src.volumes import *


class TestVolumes(TestCase):
    @params(
        (5, 125)
    )
    def test_cube(self, side, expected):
        self.assertEqual(cube(side), expected)

    @params(
        (5, 10, 15, 750)
    )
    def test_prism(self, base, deep, height, expected):
        self.assertEqual(prism(base, deep, height), expected)

    @params(
        (5, 5, 392.69908169872417)
    )
    def test_cylinder(self, height, radius, expected):
        self.assertEqual(cylinder(height, radius), expected)

    @params(
        (3, 7, 10, 70.0)
    )
    def test_pyramid(self, base, deep, height, expected):
        self.assertEqual(pyramid(base, deep, height), expected)

    @params(
        (10, 20, 2094.3951023931954)
    )
    def test_cone(self, radius, height, expected):
        self.assertEqual(cone(radius, height), expected)

    @params(
        (15, 14137.166941154068)
    )
    def test_sphere(self, radius, expected):
        self.assertEqual(sphere(radius), expected)





