""" 
import unittest
from unittest.mock import patch
from src.playagain import play_again

class TestPlayAgain(unittest.TestCase):
    @patch('builtins.input', return_value = 'No')
    @patch('main.game')
    def test_valid_answer(self, mock_game, _):
        play_again(mock_game)
        self.assertEqual(play_again(mock_game), 'Thanks for playing!')

if __name__ == '__main__':
    unittest.main() 
"""
