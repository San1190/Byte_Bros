import re

l ="g+"

if re.match(l,"g"):
    print(1)

if re.match(l,"ggggggggggg"):
    print(2)

if re.match(l, "abc"):
    print(3)