def nth_fibonacci(n):
    """
    Calculate the nth fibonacci number

    :param n: the nth fibonacci number to return
    :return:  the corresponding fibonacci number
    """
    fibonacci_numbers = [0, 1]

    if n == 0:
        return fibonacci_numbers[0]
    elif n == 1:
        return fibonacci_numbers[1]

    while len(fibonacci_numbers) < n:
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])

    return fibonacci_numbers[-1]
