x = 1
result = 0

while x <= 100:
    result += x
    x += 1
    if x % 2 == 0 :
        continue
    
    print(result)