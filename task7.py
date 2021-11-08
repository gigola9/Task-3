for i in range(1, 3):
    for j in range(1, 3):
        res = round(pow(j - pow(i, 3), 1/i))
        print(res)
