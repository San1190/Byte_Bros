try:
    print("Hello")
    print(1 / 0)

except ZeroDivisionError:
    print("Divided by zero")

finally:
    print("This code will run no matter what")