import unittest
from unittest.mock import patch
from src.intelligencesystem import system_intelligence

class TestSystemIntelligence(unittest.TestCase):
    @patch('random.randint', return_value = 7)
    def test_system_intelligence_higher(self, mock_random_number):
        hintHigherNumber = 'Tip: Try a higher number!'
        # hintLowerNumber = 'Tip: Try a lower number!'
        resultNumber = system_intelligence(5, hintHigherNumber, hintHigherNumber, 1, 10)

        self.assertEqual(resultNumber, 7)
        mock_random_number.assert_called_with(6, 10)
    
    @patch('random.randint', return_value = 2)
    def test_system_intelligence_lower(self, mock_random_number):
        # hintHigherNumber = 'Tip: Try a higher number!'
        hintLowerNumber = 'Tip: Try a lower number!'
        resultNumber = system_intelligence(5, hintLowerNumber, hintLowerNumber, 1, 10)

        self.assertEqual(resultNumber, 2)
        mock_random_number.assert_called_with(1, 4)
    
    @patch('random.randint', return_value = 6)
    def test_system_intelligence(self, mock_random_number):
        hintHigherNumber = 'Tip: Try a higher number!'
        hintLowerNumber = 'Tip: Try a lower number!'
        resultNumber = system_intelligence(5, hintLowerNumber, hintHigherNumber, 1, 10)

        self.assertEqual(resultNumber, 6)
        mock_random_number.assert_called_with(1, 10)

if __name__ == '__main__':
    unittest.main()
