"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# foo = open('src/foo.txt', 'r')
#     for x in foo:
#         print(x)
# foo.closed

with open('src/foo.txt', 'r') as f:
    read_data = f.read()
    print(read_data)

f.close()

# EXAMPLE TO PRINT WORKING DIRECTORY CONTENTS
# import os
# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # List all the files in that directory
# print("Files in %r: %s" % (cwd, files))

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

with open('src/bar.txt', 'w+') as f:
    f.write('This is one line \nThis is another line \nand another!')
f.close()