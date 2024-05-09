# Decorators
# Decorator Plus
def decor_plus(func):
    def wrap():
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        func()
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print()
    return wrap


# Decorator Minus
def decor_minus(func):
    def wrap():
        print('--------------------------------------------------------------------------------------------')
        func()
        print('--------------------------------------------------------------------------------------------')
        print()
    return wrap


# Definition function with decoration
@decor_plus
def print_nums():
    print([i for i in range(28)])


# Function
def print_chars():
    print([chr(i) for i in range(65, 91)])


# Creation of new decorated functions
#   on the basis of already defined function
print_chars_plus = decor_plus(print_chars)
print_chars_minus = decor_minus(print_chars)

# Outputting
print_nums()            # Decorated
print_chars(); print()  # Not decorated
print_chars_plus()      # Decorated
print_chars_minus()     # Decorated
