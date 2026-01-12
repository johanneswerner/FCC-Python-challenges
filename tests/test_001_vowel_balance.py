"""This module contains tests for vowel balance."""

import pytest

from challenges.id_001_vowel_balance.solution import (
    is_balanced,
)

def test_is_balanced_1():
    assert is_balanced("racecar") == True

def test_is_balanced_2():
    assert is_balanced("Lorem Ipsum") == True

def test_is_balanced_3():
    assert is_balanced("Kitty Ipsum") == False

def test_is_balanced_4():
    assert is_balanced("string") == False

def test_is_balanced_5():
    assert is_balanced(" ") == True

def test_is_balanced_6():
    assert is_balanced("abcdefghijklmnopqrstuvwxyz") == False

def test_is_balanced_7():
    assert is_balanced("123A#b!E&*456-o.U") == True
