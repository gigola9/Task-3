f = open("myFiles/data1.txt", "w")
for i in range(0, 100):
    f.write(f'\n {i}')
f.close()

