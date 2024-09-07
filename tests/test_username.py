import unittest
from src.username import user_name

class TestUserName(unittest.TestCase):
    def test_1(self):
        name = user_name("Pamela")
        self.assertEqual(name, "Pamela")