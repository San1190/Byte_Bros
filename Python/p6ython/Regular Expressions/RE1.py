import re
s = "My name is David. Hi David."
pattern = r"David"
newstr = re.sub(pattern, "Amy",s)
print(newstr)


#syntax: re.sub(pattern, repl, string, count=0)