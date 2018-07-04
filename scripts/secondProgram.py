# 2. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

# For the above assignment , trying with hard coded values to meet the need
minValue = 2002
maxValue = 3200
divisibleInput = 7
execludeInput = 5
# Defining the list and this will be printed at the end with all divisible by
# divisibleInput and not execludeInput multiple
l = []
# Taking the startIndex same as minValue
startIndex = minValue
# This boolean field will be used to determine if the first divisible is found or not.
# Until the first divisble of 7 and
# not multiple of 5 is found, we will be incrementing the startIndex by 1.
# Once it is found, then to make the program
# faster we will be incrementing the number by 7.

foundFirstDivisibleNumber = False
while startIndex <= maxValue:
    # checking if the startIndex is the number we are interested in
    if(startIndex % divisibleInput == 0 and startIndex % execludeInput != 0 ):
        # checking if the first divisible number we want is already found or not
        if(foundFirstDivisibleNumber != True):
            foundFirstDivisibleNumber = True
        # adding the number to the list
        l.append(startIndex)
    # depending on found status, incrementing either by 7 or by 1.
    if(foundFirstDivisibleNumber):
        startIndex = startIndex + 7
    else:
        startIndex = startIndex + 1
# printing the final list as a comma separated.
print("Comma separated list of numbers which are divisible by 7 and not multipliers of 5")
# printing the entire list
print(l)
# printing with a loop
for element in l:
    print(element, end=",")