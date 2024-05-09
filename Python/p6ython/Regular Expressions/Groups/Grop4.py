import re

l = r"gr(a|e)y"

match = re.match(l,"gray")

if match:
    print(1)

match = re.match(l,"grey")
if match:
    print(2)

match = re.match(l,"griy")
if match:
    print(3)

'''Another important metacharacter is |.
This means "or", so red|blue matches either "red" or "blue"'''