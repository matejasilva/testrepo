import random
import unittest
from random_utils import random_string, roll_dice, pick_random


class TestRandomString(unittest.TestCase):
    def test_length(self):
        self.assertEqual(len(random_string(5)), 5)
        self.assertEqual(len(random_string(0)), 0)
        self.assertEqual(len(random_string(20)), 20)

    def test_chars_alphanumeric(self):
        random.seed(42)
        s = random_string(100)
        self.assertTrue(all(c.isalnum() for c in s))

    def test_with_special(self):
        s = random_string(50, include_special=True)
        self.assertEqual(len(s), 50)
        valid = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*")
        self.assertTrue(all(c in valid for c in s))


class TestRollDice(unittest.TestCase):
    def test_count(self):
        random.seed(42)
        result = roll_dice(6, 5)
        self.assertEqual(len(result), 5)

    def test_range(self):
        random.seed(42)
        for _ in range(100):
            result = roll_dice(6, 1)
            self.assertGreaterEqual(result[0], 1)
            self.assertLessEqual(result[0], 6)

    def test_d20(self):
        random.seed(123)
        result = roll_dice(20, 3)
        self.assertEqual(len(result), 3)
        self.assertTrue(all(1 <= n <= 20 for n in result))


class TestPickRandom(unittest.TestCase):
    def test_returns_from_list(self):
        random.seed(99)
        items = ["a", "b", "c"]
        picked = pick_random(items)
        self.assertIn(picked, items)

    def test_empty_raises(self):
        with self.assertRaises(ValueError) as ctx:
            pick_random([])
        self.assertIn("empty", str(ctx.exception).lower())
