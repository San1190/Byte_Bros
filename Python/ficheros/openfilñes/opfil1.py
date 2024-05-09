myfile = open("filename.txt")

# write mode
open("filename.txt", "w")

# read mode
open("filename.txt", "r")
open("filename.txt")

# binary write mode
open("filename.txt", "wb")


file = open("filename.txt", "w")
# do stuff to the file
file.close()