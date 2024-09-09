import unittest
from unittest.mock import patch
from src.systemnumber import system_number

class TestSystemNumber(unittest.TestCase):
    @patch('random.randint', return_value = 32)
    def test_valid_system_number(self, mock_random_number):
        resultSystemNumber = system_number()
        self.assertEqual(resultSystemNumber, 32, 'Test failed, expected to return number 32')
        mock_random_number.assert_called_with(1, 100)

if __name__ == '__main__':
    unittest.main()
