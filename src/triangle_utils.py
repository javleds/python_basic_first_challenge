from enum import IntEnum
from triangle import Triangle


class TriangleType(IntEnum):
    Equilateral = 0
    Isosceles = 1
    Scalene = 2


def get_type(triangle: Triangle) -> TriangleType:
    triangle_sides = [
        triangle.base,
        triangle.side2,
        triangle.side3
    ]

    side_mapping = {}
    for side in triangle_sides:
        if side_mapping.get(side) is not None:
            side_mapping[side] += 1
            continue

        side_mapping[side] = 1

    for value in side_mapping.keys():
        if side_mapping[value] == 3:
            return TriangleType.Equilateral
        if side_mapping[value] == 2:
            return TriangleType.Isosceles

    return TriangleType.Scalene


def get_area(triangle: Triangle) -> float:
    half_perimeter = (triangle.base + triangle.side2 + triangle.side3) / 2
    hp_base = half_perimeter - triangle.base
    hp_side2 = half_perimeter - triangle.side2
    hp_side3 = half_perimeter - triangle.side3
    hp_result = half_perimeter * hp_base * hp_side2 * hp_side3

    return hp_result ** (1 / 2)


def get_height(triangle: Triangle) -> float:
    return (get_area(triangle) * 2) / triangle.base
