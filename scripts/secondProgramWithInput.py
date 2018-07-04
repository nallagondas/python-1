# 2. Modifying the second program to take all four variables as input, this would make the program generic
inputMinValue = int(input("Enter the minimum range number"))
inputMaxValue = int(input("Enter the max range number"))
inputDivisibleInput = int(input("Enter the divisible"))
inputExecludeInput = int(input("Enter the muliplier value to be excluded"))
# Defining the list and this will be printed at the end with all divisible by divisibleInput and not execludeInput multiple
lst = []
# Taking the startIndex same as minValue
startRange = inputMinValue
# This boolean field will be used to determine if the first divisible is found or not. Untill the first divisble of 7 and
# not multiple of 5 is found, we will be incrementing the startIndex by 1. Once it is found, then to make the program
# faster we will be incrementing the number by 7.
found = False
while startRange <= inputMaxValue:
    # checking if the startIndex is the number we are interested in
    if(startRange % inputDivisibleInput == 0 and startRange % inputExecludeInput != 0 ):
        # checking if the first divisible number we want is already found or not
        if(found != True):
            found = True
        # adding the number to the list
        lst.append(startRange)
    # depending on found status, incrementing either by 7 or by 1.
    if(found):
        startRange = startRange + inputDivisibleInput
    else:
        startRange = startRange + 1
# printing the final list as a comma seperated.
print("Comma separated list of numbers which are divisible by 7 and not multipliers of 5")
print(lst)