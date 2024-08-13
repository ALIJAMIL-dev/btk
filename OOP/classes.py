# class

class Person:
    # class attributes
    
    adress = "no informatian"
    
    #constractor (yapici method - dev... method)
    def __init__(self, name, year):
        
        # object attributes

        self.name = name
        self.year = year
        print("init ")
        # methods
    


# object
p1 = Person('ALI', 1990)
p2 = Person('Haya', 2020)

# updating

p2.name = 'HAYA'

# accessing object attributes
print(f'p1: name:{p1.name} year:{p1.year} adress: {}')
print(f'p1: name:{p2.name} year:{p2.year}')



