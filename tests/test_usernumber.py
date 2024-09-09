import unittest
from unittest.mock import patch
from src.usernumber import user_number

class TestUserNumber(unittest.TestCase):
    def test_valid_user_number(self):
        with patch('builtins.input', side_effect = ['abc', '0', '101', '7']), patch('builtins.print'):
            numberResult = user_number('7')
            self.assertEqual(numberResult, 7, 'Test failed, expected to return number 7')

if __name__ == '__main__':
    unittest.main()
