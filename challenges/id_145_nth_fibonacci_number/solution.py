"""This module deals with the calculation of the nth fibonacci number."""


def nth_fibonacci(n: int) -> int:
    """Calculate the nth fibonacci number.

    Args:
      n (int): the nth fibonacci number to return

    Returns:
        the corresponding fibonacci number
    """
    fibonacci_numbers = [0, 1]

    if n == 0:
        return fibonacci_numbers[0]
    if n == 1:
        return fibonacci_numbers[1]

    while len(fibonacci_numbers) < n:
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])

    return fibonacci_numbers[-1]
