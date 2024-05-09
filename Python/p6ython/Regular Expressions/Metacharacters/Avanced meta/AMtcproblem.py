import re
password = input()

c = r"[A-Z]+[0-9]*"

if re.search(c, password):
    print("Password created")

else:
    print("Wrong format")


#APP solution: usa pattern = r"\w*[A-Z]\w*[0-9]\w*""

