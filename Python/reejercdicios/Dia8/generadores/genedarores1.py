


def mi_generador():
    yield 4


g = mi_generador()

print(next(g))
#print(mi_generador())

def gen():
    for x in range(1,5):
        yield x * 10


def func():
    l = []
    for x in range(1,5):
        l.append(x * 10)

    return l

print(func())


g1 = gen()

print(next(g1))
print(next(g1))
print(next(g1))
print(next(g1))
