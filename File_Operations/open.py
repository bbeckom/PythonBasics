# === open can be used to load a file or export/add information to a file === #
# === file options === #
# r = open for reading (default)
# w = open for writing, truncating the file first
# x = open for exclusive creation, failing if the file already exists
# a = open for writing, appending to the end of the file if it exists
# b = binary mode
# t = text mode (default)
# + = open a disk file for updating (reading and writing)


# === example of reading a file then printing output ===#
# the second "r" options tells the opener to only read the file
myfile1 = open("myfile1.txt", "r")
# read function can be called to pull the content of the file
print("1", myfile1.read())
# close the file
myfile1.close()

# === example of writing to a file === #
mystr1 = "this is a test string\n"
# Use the "w" option to write to a given file. If the file doesn't exist it will be created.
myfile2 = open("myfile1.txt", "w")
# call the write function to add the data to the file, whatever exists in the file will be written over
myfile2.write(mystr1)
#close file
myfile2.close()
# print file contents
myfile1 = open("myfile1.txt", "r")
print("2", myfile1.read())
myfile1.close()

# === example of appending to a file === #
# "a" option sets the open mode to append, meaning info will be added to end of the file instead of
# overwriting existing information
myfile3 = open("myfile1.txt", "a")
# create a new string then just add to the end of the file twice
mystr2 = "appended info\n"
myfile3.write(mystr2)
myfile3.write(mystr2)
# close file
myfile3.close()
# print file contents
myfile1 = open("myfile1.txt", "r")
print("3", myfile1.read())
myfile1.close()