import re
s = int(input())
if s[0] == 0:
    if s[1] == 0:
        pattern = r"00"

        newstr = re.sub(pattern, "+", s, count=1)

        print(newstr)
    
    else: 
        print("Error")

else:
    print("Error")
#your code goes here


