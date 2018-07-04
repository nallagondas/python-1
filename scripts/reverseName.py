# 3. Write a Python program to accept the user's first and last name and then getting them printed in the the
# reverse order with a space between first name and last name.
# writing the program without using any build functions or easy commands.
firstName = input("Enter your first name")
lastName = input("Enter your last name")
print("Name you entered :" + firstName + " " + lastName)
# getting lenth for both first and last name
firstNameLen = len(firstName)
lastNameLen = len(lastName)
# variables to store the reversted strings
revFirstName = ""
revLastName = ""
# looping through the
for i in range(firstNameLen - 1, -1, -1):
    revFirstName += firstName[i]

for i in range(lastNameLen - 1, -1, -1):
    revLastName += lastName[i]

print("Reverse of your first and lastname with a space in the middle  :: " + revFirstName + " " + revLastName)

# The same above can be done in two lines or one line.

print ("Reverse of your first and lastname with a space in the middle using string manipulation functions :: "
       +firstName[::-1] + " " + lastName[::-1])
