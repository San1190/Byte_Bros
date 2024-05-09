import re
pattern = r"^gr.y$"#for start and finish the line 

if re.match(pattern,"grey"):
    print("Match 1")

if re.match(pattern, "gray"):
    print("Match 2")

if re.match(pattern, "stingray"):
    print("Match 3")