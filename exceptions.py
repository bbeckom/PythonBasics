# you can use try/except to catch errors and perform actions

myvalue = "this is a string"

# attempt to convert the string to an int (not possible)
try:
    # this will fail because the string can't be converted to a number
    int(myvalue)
# most basic way to catch exception (this will even capture ctrl+c so be careful if looping)
except:
    print("ERROR")


try:
    int(myvalue)
# can capture the exception and print output with info about the type of exception
except Exception as diag:
    print(diag.__class__.__name__, ':', diag)

try:
    int(myvalue)
# can also just call plainly
except Exception:
    print("GENERIC ERROR")


try:
    int(myvalue)
# or more specifically choose exception type
except ValueError:
    print("YOU GOT A ValueError")
