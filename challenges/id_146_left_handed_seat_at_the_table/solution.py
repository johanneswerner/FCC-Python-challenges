"""This module deals with determining the number of left-handed seats at the table."""


def find_left_handed_seats(table: list[list[str]]) -> int:
    """Determine the number of left handed seats at the table.

    Args:
        table (list[list[str]]): The seating arrangement at the table, where each
        sublist represents a row of seats. Each element in the sublist is either 'U'
        for an upright position, 'L' for a left-handed position, or 'R' for a
        right-handed position. The imaginary persons in the upper list are facing down,
        the imaginary persons in the lower list are facing up.

    Returns:
        int: The number of left handed seats at the table.
    """
    result = 0
    table[0].reverse()

    for sublist in table:
        if sublist[0] == "U":
            result += 1
        for i in range(len(sublist) - 1):
            if sublist[i] != "R" and sublist[i + 1] == "U":
                result += 1

    return result
