myinput = "test input"
# you can use % formatting to get variables inside quotes
# %s is for string
print("Here is a string - '%s'" % myinput)
# %d is for int
# you can pass multiple variables at once
myint = 1
myinput2 = "second string"
print("Here is a number - %d\n"
      "Here is another string - '%s'" % (myint,myinput2))
