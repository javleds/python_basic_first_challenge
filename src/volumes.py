from math import pi


def cube(side: float) -> float:
    return side ** 3


def prism(base: float, deep: float, height: float) -> float:
    return base * height * deep


def cylinder(radius:  float, height: float) -> float:
    return pi * (radius ** 2) * height


def pyramid(base: float, deep: float, height: float) -> float:
    return (base * deep * height) / 3


def cone(radius: float, height: float) -> float:
    return (pi * (radius ** 2) * height) / 3


def sphere(radius: float) -> float:
    return (4 / 3) * pi * (radius ** 3)

