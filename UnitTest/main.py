# default value of '' is entered if nothing is provided in function call
def DivideByTwo(myinput=''):
    while True:
        if myinput == '':
            myinput = input("Enter a number to divide by 2\n"
                            ":")
        try:
            # convert to int
            myinput = int(myinput)
            result = myinput/2
            # return value and end loop
            return result
        # put Exception so that ctrl+c can still be captured
        except Exception:
            print("Input needs to be a number!\n")
            # blank out value so it asks for input
            myinput = ''
            # restart the loop
            continue
