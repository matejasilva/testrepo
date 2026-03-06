#!/usr/bin/env python3
"""Random utilities - a collection of small helper functions."""

import random
import string


def random_string(length: int = 10, include_special: bool = False) -> str:
    """Generate a random string of given length."""
    chars = string.ascii_letters + string.digits
    if include_special:
        chars += "!@#$%^&*"
    return "".join(random.choices(chars, k=length))


def roll_dice(sides: int = 6, count: int = 1) -> list[int]:
    """Roll dice and return the results."""
    return [random.randint(1, sides) for _ in range(count)]


def pick_random(items: list) -> str | int | float:
    """Pick a random element from a list."""
    if not items:
        raise ValueError("Cannot pick from empty list")
    return random.choice(items)


if __name__ == "__main__":
    print("Random string:", random_string())
    print("Dice roll (3d6):", roll_dice(6, 3))
    print("Random pick:", pick_random(["apple", "banana", "cherry"]))
