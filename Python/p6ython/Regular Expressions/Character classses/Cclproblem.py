import re
Id = input()

f =r"^[A-Z][A-Z][0-9][0-9]$"

if re.search(f,Id):
    print("Searching")

else:
    print("Wrong format")