def fun( x , y = 7, *args , **kwargs):
    print(kwargs)

fun(2,3,4,5,6, a = 7, b = 8)