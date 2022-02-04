""" LEGB
Local, Enclosing, Global, Built-in """

x = 'global x'

def test():
    global x
    x = 'local x'
    #y = 'local y'
    #print(y)
    print(x)
test()
print(x)

def test(z):
    x = 'local x'
    print(z)
test('local z')

import builtins
print(dir(builtins))


def outer():
    x = 'outer x'

    def inner():
        x = 'inner x'
        print(x)
    inner()
    print(x)

outer()


def outer():
    x = 'outer x'

    def inner():
        nonlocal x
        x = 'inner x'
        print(x)
    inner()
    print(x)

outer()