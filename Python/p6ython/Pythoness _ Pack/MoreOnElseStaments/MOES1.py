for i in range(10):
    if i == 999:
        break

else:
    print("Unbroken 1")

for i in range(10):
    if i == 5:
        break

else:
    print("Unbroken 2")

'''The first for loop executes normally, resulting in the printing of "Unbroken 1".
The second loop exits due to a break, which is why it's else statement is not executed.'''