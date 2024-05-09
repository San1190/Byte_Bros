#-------------------------------
msg = "Hello world!"
file = open("newfile", "w")
amount_written = file.write(msg)
print(amount_written)
file.close()
