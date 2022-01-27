def ex119():
    x = 1.0
    for i in range(20):
        x = x/3
    for i in range(20):
        x = x*3
    return x


from random import*

def  ex220():
    acc = 0
    for i in range(1000000):
        x = uniform(0, 1)
        y = uniform(0, 1)
        if x**2 + y**2 <= 1:
            acc += 1
    pi = acc/1000000 * 4
    return pi


def ex221():
    x = 2.0**52
    return x+1


def ex222():
    x = 2**47
    return 2.0**100 + x == 2.0**100
        