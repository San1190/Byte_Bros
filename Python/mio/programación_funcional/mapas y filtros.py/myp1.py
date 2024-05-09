def add_five(x):
    return x + 5

nums = [11,22,33,44,55]
result = list(map(add_five, nums))
print(result)



"""The built-in functions map and filter are very useful higher-order functions that operate on lists (or similar objects called iterables).
The function map takes a function and an iterable as arguments, and returns a new iterable with the function applied to each argument."""



#using Lambda suntax

num = [11,22,33,44,55]
results = list(map(lambda x: x+5 , num))
print (results)