"""This module deals with determining if the string is balanced."""

VOWELS = set("aeiou")


def is_balanced(s: str) -> bool:
    """Check if a string is balanced.

    A string is balanced if the number of vowels in the first half of the string is
    equal to the number of vowels in the second half of the string. If the string
    length is odd, the middle character is ignored.

    Args:
        s: The string to check.

    Returns:
        True if the string is balanced, False otherwise.
    """
    s = s.lower()
    s1 = s[: len(s) // 2]
    s2 = s[(len(s) + 1) // 2 :]

    sum1 = sum(1 for c in s1 if c in VOWELS)
    sum2 = sum(1 for c in s2 if c in VOWELS)

    return sum1 == sum2
