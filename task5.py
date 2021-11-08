import random

a = int(input("შეიყვანეთ პირველი რიცხვი: "))
b = int(input("შეიყვანეთ მეორე რიცხვი: "))

f = open("myFiles/data2.txt", "w")

for i in range (0, 100):
    f.write(f'\n {random.randint(a, b)}')

f.close()
