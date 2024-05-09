from nis import match
import re
text = input()

h = r"#\w+"

m = re.findall(h, text)

if m:
    print("\n".join(m))

#.join takes all items in an iterable and joins them into one string. A string must be specified as the separator.
#your code goes here
#use re.findall() with r"#\w+" as the regex
