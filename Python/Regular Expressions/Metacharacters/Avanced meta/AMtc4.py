import re

l =r"9{1,3}$"

if re.match(l, "9"):
    print(1)

if re.match(l,"999"):
    print(2)
if re.match(l,"9999"):
    print(3)

#"9{1,3}$" matches string that have 1 to 3 nines.