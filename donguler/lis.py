say = int(input("sayi: "))
asalmi = True

if say == 1:
    print("1 dioony")

for i in range(2, say):
    if (say % i == 0):
        asalmi = False
        break

if asalmi:
    print("sayi t00")

else:
    print("sayi f00")