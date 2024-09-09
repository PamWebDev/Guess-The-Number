import unittest
from unittest.mock import patch
from src.username import user_name

class TestUserName(unittest.TestCase):
    def test_valid_usename(self):
        with patch('builtins.input', side_effect = ['5','&@/.', 'Pam']), patch('builtins.print'):
            result = user_name('Pam')
            self.assertEqual(result, 'Pam', 'Test failed, expected to return "Pam"')

if __name__ == '__main__':
    unittest.main()
