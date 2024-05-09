import re

word = input()

let =r"^m..e$"

if re.match(let, word):
    print("Match")
else:
    print("No match")