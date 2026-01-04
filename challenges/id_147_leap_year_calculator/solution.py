"""This module deals with determining if the number is a leap year."""


def is_leap_year(year: int) -> bool:
    """Check if a year is a leap year.

    Args:
        year (int): The year to check.

    Returns:
        A boolean indicating whether the year is a leap year.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
