'''Using *args as a function parameter enables you to pass an arbitrary number of arguments to that function. The arguments are then accessible as the tuple args in the body of the function.'''

def fun(named_arg, *args):
    print(named_arg)
    print(args)

fun(1,2,3,4,5)