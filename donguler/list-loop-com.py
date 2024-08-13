import random

say = random.randint(1, 100)
hak = 5

while hak > 0:
    hak -= 1
    tahmin = int(input("tahmin : "))

    if say == tahmin:
        print("What!")
        break

    elif say > tahmin:
        print("yukari")
    
    else:
        print("asagi")

    if hak == 0:
        print(f"hak ended {say}")