"""This module contains tests for find left handed seats at the table."""

import pytest
from challenges.id_146_left_handed_seat_at_the_table.solution import find_left_handed_seats


def test_find_left_handed_seats_1():
    assert find_left_handed_seats([["U", "R", "U", "L"], ["U", "R", "R", "R"]]) == 2

def test_find_left_handed_seats_2():
    assert find_left_handed_seats([["U", "U", "U", "U"], ["U", "U", "U", "U"]]) == 8

def test_find_left_handed_seats_3():
    assert find_left_handed_seats([["U", "R", "U", "R"], ["L", "R", "R", "U"]]) == 0

def test_find_left_handed_seats_4():
    assert find_left_handed_seats([["L", "U", "R", "R"], ["L", "U", "R", "R"]]) == 1

def test_find_left_handed_seats_5():
    assert find_left_handed_seats([["U", "R", "U", "U"], ["U", "U", "L", "U"]]) == 5
