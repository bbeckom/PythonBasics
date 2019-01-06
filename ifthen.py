# simple if statement to check if variable is equal to something
# using elif to show that only one of these should run
# can also use >= or <=
myvar = 1
if myvar == 1:
    print("Yes")
elif myvar > 1:
    print("Greater than 1")
elif myvar < 0:
    print("Less than 0")

# shows not equal to
myvar2 = 3
if myvar2 != 3:
    print("Not 3")

# use else to trigger when if statement fails
if myvar2 == 4:
    print("Is 4")
else:
    print("Not 4")
