sayilar = [1,3,5,7,9,12,19,21]

###

i0 = 0

while (i0 < len(sayilar)):
    print(sayilar[i0])
    i0 += 1

###

b1 = int(input('b1: '))
s1 = int(input('s1 : '))
i2 = b1
while i2 < s1:
    i2 += 1
    if (i2 % 2 == 1):
        print(i2)

###

i1 = 100

while i1 > 0:
    i1 -= 1
    print(i1)