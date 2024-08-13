# global scope
x = 'global x'

def function():
    # local scope
    # x = 'local x'
    print(x)

function()
print(x)

########################################################
#global
name = 'Cinar'

def ch(new_name):
    # local
    name = new_name
    print(name)

ch('ADAda')
print(name)

#########################################################

name = 'global string'

def gret():
    #name = 'local string'

    def h():
        # name = 'ada'
        print('hello' + name)

    h()

gret()


#############################################################

x = 50
def test():
    global x
    print(f'x {x}')

    x = 100
    print(f'change x to {x}')

test()