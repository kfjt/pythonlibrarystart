from unittest import TestCase

from package1 import module1


class TestModule1(TestCase):
    def test_hello(self):
        actual = module1.hello("world")
        expected = "hello world"
        self.assertEqual(actual, expected)
