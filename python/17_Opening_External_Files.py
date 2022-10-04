# Building Translator in Python
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


def dev_profile():
    profile = open("myProfile.txt", "r")  # 'r' for read,'w' for write, 'r+' for read/write and 'a' for append
    print(profile.read())
    profile.close()  # It is Best practice to always close your file after using it


#  Writing and Appending to Files

userName = input("Enter Username: ")
passWord = input("Enter Password: ")

print()
auth_File = open("auth_File.txt", "a")
auth_File.write(userName + ", ")
auth_File.write(passWord + ", ")
auth_File.write("\n")
auth_File.close()
print("Your Credentials Saved Successfully!")
print()
dev_profile()
print()


#  Another simpler way of reading a file line-by-line and printing them is shown below using FOR - LOOP
"""
developer_Profile = open("myProfile.txt", "r+")
for line in developer_Profile.readlines():
    print(line)
developer_Profile.close()
"""

#  Another simpler way of reading a file line-by-line and printing them is shown below using If-Else
"""
profile = open("myProfile.txt", "r")  # 'r' for read,'w' for write, 'r+' for read/write and 'a' for append
    if profile.readable():  # Checking for file readability
        print(profile.read())
    else:
        print("File not readable")
    profile.close()  # It is Best practice to always close your file after using it
"""

# Creating an UPPERCASE itsy spider outfile

infile = open("spider.txt", "r")
outfile = open("upSpider.txt", "w")

for aline in infile:
    newline = aline.upper()
    print(newline)
    outfile.write(newline)
outfile.close()
infile.close()

