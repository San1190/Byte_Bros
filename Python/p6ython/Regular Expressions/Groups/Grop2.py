import re

l = r"a(bc)(de)(f(g)h)i"

match = re.match(l, "abcdefghijklmnop")

if match:
    print(match.group())
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.groups())