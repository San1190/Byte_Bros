import re

l = r"(\D+\d)"

match = re.match(l, "Hi 999!")

if match:
    print(1)

match = re.match(l,"1, 23, 456!")

if match:
    print(2)

match = re.match(l, " ! $?")

if match:
    print(3)

'''

More useful special sequences are \d, \s, and \w.
These match digits, whitespace, and word characters respectively.
In ASCII mode they are equivalent to [0-9], [ \t\n\r\f\v], and [a-zA-Z0-9_].
In Unicode mode they match certain other characters, as well. For instance, \w matches letters with accents.
Versions of these special sequences with upper case letters - \D, \S, and \W - mean the opposite to the lower-case versions. For instance, \D matches anything that isn't a digit.'''