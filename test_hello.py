import unittest
from src.hello import greet

class TestGreetFunction(unittest.TestCase):
    def test_default_greeting(self):
        self.assertEqual(greet(), "Hello, world.")

    def test_custom_greeting(self):
        self.assertEqual(greet("23 skidoo"), "23 skidoo")

    def test_empty_string(self):
        self.assertEqual(greet(""), "")

if __name__ == '__main__':
    unittest.main()