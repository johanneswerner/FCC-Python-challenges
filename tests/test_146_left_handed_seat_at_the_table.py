"""This module contains tests for find left handed seats at the table."""

import pytest

from challenges.id_146_left_handed_seat_at_the_table.solution import (
    find_left_handed_seats,
)


@pytest.mark.parametrize(
    ("seat_order", "expected"),
    [
        ([["U", "R", "U", "L"], ["U", "R", "R", "R"]], 2),
        ([["U", "U", "U", "U"], ["U", "U", "U", "U"]], 8),
        ([["U", "R", "U", "R"], ["L", "R", "R", "U"]], 0),
        ([["L", "U", "R", "R"], ["L", "U", "R", "R"]], 1),
        ([["U", "R", "U", "U"], ["U", "U", "L", "U"]], 5),
    ],
    ids=[
        "first seat order",
        "second seat order",
        "third seat order",
        "fourth seat order",
        "fifth seat order",
    ],
)
def test_find_left_handed_seats(seat_order: list[list[str]], expected: int) -> None:
    """Test find left handed seats at the table."""
    assert find_left_handed_seats(seat_order) == expected
