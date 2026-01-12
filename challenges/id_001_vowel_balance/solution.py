"""This module deals with determining if the string is balanced."""


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
    vowels = set("aeiou")
    s = s.lower()
    length = len(s)
    first_list = s[: length // 2]
    second_list = s[(length + 1) // 2 :]

    sum1, sum2 = 0, 0
    for first_elem, second_elem in zip(first_list, second_list, strict=True):
        if first_elem in vowels:
            sum1 += 1
        if second_elem in vowels:
            sum2 += 1

    return sum1 == sum2
