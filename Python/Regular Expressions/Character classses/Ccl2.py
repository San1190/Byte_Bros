import re

l = r"[A-Z][A-Z][0-9]"

if re.search(l,"LS8"):
    print(1)

if re.search(l,"E3"):
    print(2)

if re.search(l,"1ab"):
    print(3)