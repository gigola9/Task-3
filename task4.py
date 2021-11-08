for i in range(1, 31):
    f = open(f"myFiles2/file{i}.txt", "w")
    f.write(f'Programmer{i}')
    f.close()

