import re

l =r"[aeiou]"#The pattern [aeiou] in the search function matches all strings that contain any one of the characters defined.

if re.search(l, "grey"):
    print(1)
if re.search(l,"qwertyuiop"):
    print(2)
if re.search(l,"rhythm myths"):
    print(3)

'''The class [a-z] matches any lowercase alphabetic character.
The class [G-P] matches any uppercase character from G to P.
The class [0-9] matches any digit.
Multiple ranges can be included in one class. For example, [A-Za-z] matches a letter of any case.'''