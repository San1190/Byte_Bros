f = open("newfile.txt", "w")

f.write("This has been written to a file")
f.close()

f = open("newfile.txt", "r")
print(f.read())
f.close()


#-------------------------------------------------------
file = open("newfile.txt", "r")
print("Reading inital contents")
print(file.read())
print("Finished")
file.close()

file = open("newfile.txt", "w")
file.write("Some new text")
file.close()

file = open("newfile.txt", "r")
print("Reading new contents")
print(file.read())
print("Finished")
file.close()

#-------------------------------
msg = "Hello world!"
file = open("newfile", "w")
amount_written = file.write(msg)
print(amount_written)
file.close()


