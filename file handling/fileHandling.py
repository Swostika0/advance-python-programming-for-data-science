#opening file in read mode
'''f = open("/workspaces/advance-python-programming-for-data-science/file handling/file.txt", "r")
content = f.read()
print(content)
f.close()

#readline()
print(f.readline())

#readlines()
print(f.readlines())'''

#writing to a file-->w mode deletes previous content!
f = open("/workspaces/advance-python-programming-for-data-science/file handling/file.txt", "w")
f.write("Hello ! that pihu is actually me")
f.close()

#appending to the file
f = open("/workspaces/advance-python-programming-for-data-science/file handling/file.txt", "a")
f.write("\nNew line added")
f.close()

#to close the file automatically we can use with syntax
with open("/workspaces/advance-python-programming-for-data-science/file handling/file.txt", "r") as f:
    print(f.read())

"""Deleting a File--> os is inbuilt library in python
import os
os.remove("data.txt")"""