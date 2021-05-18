from unittest import TestCase
from unittest.mock import patch
from src.input_utils import ask_for_number


class TestInputUtils(TestCase):
    @patch('builtins.input', return_value='1')
    def test_ask_for_number(self, input):
        self.assertEqual(ask_for_number(''), 1.0)
