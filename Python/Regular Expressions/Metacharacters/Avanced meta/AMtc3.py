import re

l = r"ice(-)?cream"

if re.match(l, "ice-cream"):
    print(1)

if re.match(l,"icecream"):
    print(2)

if re.match(l,"sausages"):
    print(3)

if re.match(l,"ice--ice"):
    print("4")

#The metacharacter ? means "zero or one repetitions".