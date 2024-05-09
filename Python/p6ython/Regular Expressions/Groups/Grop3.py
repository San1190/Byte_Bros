
import re

l = r"(?P<firts>abc)(?:def)(ghi)"

match = re.match(l, "abcdefghi")

if match:
    print(match.group("firts"))
    print(match.groups())

'''There are several kinds of special groups.
Two useful ones are named groups and non-capturing groups.
Named groups have the format (?P<name>...), where name is the name of the group, and ... is the content. They behave exactly the same as normal groups, except they can be accessed by group(name) in addition to its number.
Non-capturing groups have the format (?:...). They are not accessible by the group method, so they can be added to an existing regular expression without breaking the numbering.'''