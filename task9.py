for i in range(1, 10001):
    f = open(f"myFiles/{i}.txt", "w")
    f.write(f'{i}')
    f.close()

