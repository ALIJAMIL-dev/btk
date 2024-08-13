def add(*params):
    return sum((params))

print(add(10, 20, 50, 40))

def displayuser(**args): # *params or *args = tuple but **params or **args = dinc
    print(type(args))
    for key, value in args.items():
        print('{} is {}'.format(key, value))


displayuser(name = 'Cnr', age = 2, city = "istanbul")
displayuser(name = 'Can', age = 13, city = "Kocaeli", phone = 123321231)
displayuser(name = 'Car', age = 18, city = "Ankara", phone = 123321231, email = 'ali@gmil.com')

def myfunc(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(*args)
    print(**kwargs)
    