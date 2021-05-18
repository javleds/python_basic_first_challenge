from number_utils import is_float


def ask_for_number(message: str) -> float:
    while True:
        value = input(message)
        if is_float(value):
            break

        if value.lower() == 'q':
            exit('See you...')

        print('Invalid character, please type a number. Or press `q` to exit')

    return float(value)
