from triangle import Triangle
from triangle_utils import get_type, get_area, get_height
from input_utils import ask_for_number

if __name__ == '__main__':
    triangle = Triangle(
        ask_for_number('Please insert the base length: '),
        ask_for_number('Please insert the side2 length: '),
        ask_for_number('Please insert the side3 length: ')
    )
    print('The triangle is {}, it\'s area is {} and it\'s height is {}'.format(
        get_type(triangle),
        get_area(triangle),
        get_height(triangle)
    ))
