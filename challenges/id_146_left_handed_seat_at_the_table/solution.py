def find_left_handed_seats(table):
    result = 0
    table[0].reverse()

    for sublist in table:
        if sublist[0] == "U":
            result += 1
        for i in range(len(sublist) - 1):
            if sublist[i] != "R" and sublist[i+1] == "U":
                result += 1

    return result
