import pytest

from challenges.id_145_nth_fibonacci_number.solution import nth_fibonacci


def test_nth_fibonacci_4():
    assert nth_fibonacci(4) == 2

def test_nth_fibonacci_10():
    assert nth_fibonacci(10) == 34

def test_nth_fibonacci_15():
    assert nth_fibonacci(15) == 377

def test_nth_fibonacci_40():
    assert nth_fibonacci(40) == 63245986

def test_nth_fibonacci_75():
    assert nth_fibonacci(75) == 1304969544928657
