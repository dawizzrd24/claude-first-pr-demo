import unittest

from greet import greet


class TestGreet(unittest.TestCase):
    def test_greet_returns_expected_message(self):
        self.assertEqual(greet("world"), "Hello, world!")

    def test_greet_uses_given_name(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")


if __name__ == "__main__":
    unittest.main()
