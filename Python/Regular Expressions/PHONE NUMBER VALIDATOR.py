import re

usernum = input()
num = r"^(1|8|9)\d{7}$" # modo no churro

#num = r"^(1|8|9).......$" # modo churro

if re.match(num, usernum):
    print("Valid")

else:
    print("Invalid")