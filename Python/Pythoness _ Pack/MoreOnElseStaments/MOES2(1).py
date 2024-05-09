try:
    print(1)

except ZeroDivisionError:
    print(2)
else:
    print(3)

try:
    print(1/0)

except ZeroDivisionError:
    print(4)
else:
    print(5)