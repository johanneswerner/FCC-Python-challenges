"""This module contains tests for confirming adequate tire pressure."""

import pytest

from challenges.id_148_tire_pressure.solution import (
    tire_status,
)

@pytest.mark.parametrize(
    ("pressures_psi", "range_bar"),
    [
        ([32, 28, 35, 29], [2, 3]),
        ([32, 28, 35, 30], [2, 2.3]),
        ([29, 26, 31, 28], [2.1, 2.5]),
        ([31, 31, 30, 29], [1.5, 2]),
        ([30, 28, 30, 29], [1.9, 2.1]),
    ],
    ids=[
        "tire_status_1",
        "tire_status_2",
        "tire_status_3",
        "tire_status_4",
        "tire_status_5",
    ]
)
def test_tire_pressure(pressures_psi: list, range_bar: list) -> None:
    """Test tire status."""
    assert tire_status(pressures_psi, range_bar)
