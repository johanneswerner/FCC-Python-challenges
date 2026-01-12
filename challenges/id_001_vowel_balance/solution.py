def is_balanced(s):
    vowels = set("aeiou")
    s = s.lower()
    length = len(s)
    first_list = s[:length // 2]
    second_list = s[(length + 1) // 2:]

    sum1, sum2 = 0, 0
    for first_elem, second_elem in zip(first_list, second_list):
        if first_elem in vowels:
            sum1 += 1
        if second_elem in vowels:
            sum2 += 1

    return sum1 == sum2
