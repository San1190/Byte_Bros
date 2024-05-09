from re import X


def gen():
    x = 1

    yield X

    x += 1

    yield X

    x += 1

    yield X


g = gen()

print(next(g))
print(next(g))
print(next(g))
