import re




num = "07987549836"

pattern = r"9"

num = re.sub(pattern,"0",num)

print(num)