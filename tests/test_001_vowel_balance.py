"""This module contains tests for vowel balance."""

import string

import pytest

from challenges.id_001_vowel_balance.solution import (
    is_balanced,
)


@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("racecar", True),
        ("Lorem Ipsum", True),
        ("Kitty Ipsum", False),
        ("string", False),
        (" ", True),
        (string.ascii_lowercase, False),
        ("123A#b!E&*456-o.U", True),
    ],
    ids=[
        "racecar",
        "Lorem Ipsum",
        "Kitty Ipsum",
        "string",
        "space",
        "alphabet",
        "mixed",
    ],
)
def test_is_balanced(s: str, expected: bool) -> None:  # noqa: FBT001
    """Test is_balanced function."""
    assert is_balanced(s) == expected
