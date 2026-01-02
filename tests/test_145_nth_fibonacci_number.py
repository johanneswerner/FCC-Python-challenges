"""This module contains tests for the nth fibonacci number calculation."""

import pytest

from challenges.id_145_nth_fibonacci_number.solution import nth_fibonacci


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (4, 2),
        (10, 34),
        (15, 377),
        (40, 63245986),
        (75, 1304969544928657),
    ],
    ids=[
        "4th fibonacci",
        "10th fibonacci",
        "15th fibonacci",
        "40th fibonacci",
        "75th fibonacci",
    ],
)
def test_nth_fibonacci(n: int, expected: int) -> None:
    """Test nth fibonacci number."""
    assert nth_fibonacci(n) == expected
