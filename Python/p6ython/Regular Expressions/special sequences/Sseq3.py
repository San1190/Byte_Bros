import re

l = r"\b(cat)\b"

match = re.search(l, "The cat sat!")

if match:
    print(1)

match = re.search(l,"We s>cat<tered?")

if match:
    print(2)

match = re.search(l, "We scattered.")

if match:
    print(3)


'''\b(cat)\b" basically matches the word "cat" surrounded by word boundaries.'''


'''
Additional special sequences are \A, \Z, and \b.
The sequences \A and \Z match the beginning and end of a string, respectively.
The sequence \b matches the empty string between \w and \W characters, or \w characters and the beginning or end of the string. Informally, it represents the boundary between words.
The sequence \B matches the empty string anywhere els'''