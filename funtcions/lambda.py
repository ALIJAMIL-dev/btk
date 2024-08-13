# def square(num): # return num ** 2
#     return num ** 2
square = lambda num: num ** 2
nmbr = [1,3,5,9,10,4]

print(list(map(square, nmbr))) #result = lambda num: num ** 2, nmbr
#         =       
# for ny in nmbr:
#     print(square(ny))

def check(num): # return num %2 == 0
    return num % 2 == 0

# list(filter(check, nmbr))
print(list(filter(lambda num: num % 2 == 0)))