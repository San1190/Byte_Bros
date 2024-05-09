import re

l = r"egg(spam)*"

if re.match(l,"egg"):
    print(1)
if re.match(l,"eggspamegg"):
    print(2)
if re.match(l,"spam"):
    print(3)

#The example above matches strings that start with "egg" and follow with zero or more "spam"s.