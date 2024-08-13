# # class

# class Person:
#     # class attributes
    
#     adress = "no informatian"
    
#     #constractor (yapici method - dev... method)
#     def __init__(self, name, year):
        
#         # object attributes

#         self.name = name
#         self.year = year
#         # instances methods

#         def intro(self):
#             print("Hello There")

#         def calculateAge(self):
#             return 2019 - self.year
    
# # object
# p1 = Person('ALI', 1990)
# p2 = Person('Haya', 2020)






class circle:
    pi = 3.14

    def __init__(self, yaricap=1):
        self.yaricap = yaricap

    def cevre_hesap(self):
        return 2*self.pi+self.yaricap
    
    def alan_hesap(self):
        return self.pi*(self.yaricap**2)
    
c1 = circle() # yaricap 1
c2 =circle(5)

print(f"c1 = alan {c1.alan_hesap()} cevre {c1.cevre_hesap}")
print(f"c2 = alan {c2.alan_hesap()} cevre {c2.cevre_hesap}")
