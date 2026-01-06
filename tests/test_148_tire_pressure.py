"""This module contains tests for confirming adequate tire pressure."""

import pytest

from challenges.id_148_tire_pressure.solution import (
    tire_status,
)

def test_tire_status_1():
    assert tire_status([32, 28, 35, 29], [2, 3]) == ["Good", "Low", "Good", "Low"]

def test_tire_status_2():
    assert tire_status([32, 28, 35, 30], [2, 2.3]) == ["Good", "Low", "High", "Good"]

def test_tire_status_3():
    assert tire_status([29, 26, 31, 28], [2.1, 2.5]) == ["Low", "Low", "Good", "Low"]

def test_tire_status_4():
    assert tire_status([31, 31, 30, 29], [1.5, 2]) == ["High", "High", "High", "Good"]

def test_tire_status_5():
    assert tire_status([30, 28, 30, 29], [1.9, 2.1]) == ["Good", "Good", "Good", "Good"]
