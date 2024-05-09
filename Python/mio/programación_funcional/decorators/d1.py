def decor(func):
    print("_ _ _ _ _ _ _ _ _ _ \n")
    func()
    print("_ _ _ _ _ _ _ _ _ _")

@decor
def hello_world():
    print("Hello World")

"""_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _"""

def hello():
    print("Hello")

decor(hello)





#def decor(func):
#    def warp():
#        print("===========")
#        func()
#        print("===========")
#    return warp
#
#def print_text():
#    print("Hello Wolrd")
#
#decorated = decor(print_text)
#decor()