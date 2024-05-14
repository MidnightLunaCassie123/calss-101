import random
response="y"

while response=="y":

    no=random.randint(1,6)

    if no==1:
        print("_______")
        print("|     |")
        print("|     |")
        print("|  0  |")
        print("|     |")
        print("|-----|")
    if no==2:
        print("_______")
        print("| 0   |")
        print("|     |")
        print("|    0|")
        print("|     |")
        print("|-----|")
    if no==3:
        print("_______")
        print("| 0   |")
        print("|     |")
        print("|  0  |")
        print("|    0|")
        print("|-----|")
    if no==4:
        print("_______")
        print("| 0  0|")
        print("|     |")
        print("|   0 |")
        print("| 0   |")
        print("|-----|")
    if no==5:
        print("_______")
        print("|   0 |")
        print("| 0  0|")
        print("|  0  |")
        print("| 0   |")
        print("|-----|")
    if no==6:
        print("_______")
        print("|  00 |")
        print("|  0  |")
        print("|  0  |")
        print("|  00 |")
        print("|-----|")

    response=input("Press y to roll again and n to exit")
    print("/n")