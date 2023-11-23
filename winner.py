def checkwin(area, draw):
    check = {}
    for i in area:
        check[i.name] = i.own

    if check[1] == check[5] == check[21] == check[25] and check[1] != 0:
        return check[1]
    if check[1] == check[7] == check[13] == check[19] == check[25] and check[1] != 0:
        return check[1]
    if check[5] == check[9] == check[13] == check[17] == check[21] and check[5] != 0:
        return check[5]
    for i in range(5):
        if check[1 + (i*5)] == check[2 + (i*5)] == check[3 + (i*5)] == check[4 + (i*5)] == check[5 + (i*5)] and check[1 + (i*5)] != 0:
            return check[1 + (i*5)]
        if check[1 + i] == check[6 + i] == check[11 + i] == check[16 + i] == check[21 + i] and check[1 + i] != 0:
            return check[1 + i]
    if draw >= 30:
        return 3