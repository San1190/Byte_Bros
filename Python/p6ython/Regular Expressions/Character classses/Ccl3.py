import re
l = r"[^A-Z]"

if re.search(l,"this is all quiet"):
    print(1)

if re.search(l,"AbCdEfG123"):
    print(2)

if re.search(l,"THISISALLSHOUTING"):
    print(3)
 
'''The pattern [^A-Z] excludes uppercase strings.
Note, that the ^ should be inside the brackets to invert the character class.'''