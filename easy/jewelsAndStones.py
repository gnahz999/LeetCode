def jas(J, S):
    jewels = set(J)
    count = 0

    for x in S:
        if x in J:
            count += 1

    return count