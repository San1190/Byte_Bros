import re

l = r"(.+) \1"

match = re.match(l, "word word")

if match:
    print(1)

match = re.match(l,"?! ?!")

if match:
    print(2)

match = re.match(l, "abc cde")

if match:
    print(3)


'''Note, that "(.+) \1" is not the same as "(.+) (.+)", because \1 refers to the first group's subexpression, which is the matched expression itself, and not the regex pattern.'''