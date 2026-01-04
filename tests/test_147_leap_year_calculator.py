"""This module contains tests for find left handed seats at the table."""

import pytest
from challenges.id_147_leap_year_calculator.solution import (
    is_leap_year,
)


@pytest.mark.parametrize(
    ("year", "expected"),
    [
        (2024, True),
        (2023, False),
        (2100, False),
        (2000, True),
        (1999, False),
        (2040, True),
        (2026, False),
    ],
    ids=[
        "leap year - 2024",
        "not leap year - 2023",
        "not leap year - 2100",
        "leap year - 2000",
        "not leap year - 1999",
        "leap year - 2040",
        "not leap year - 2026",
    ],
)
def test_is_leap_year(year: int, expected: bool) -> None:  # noqa: FBT001
    """Test is leap year."""
    assert is_leap_year(year) == expected
