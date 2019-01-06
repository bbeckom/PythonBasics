# functions are defined with 'def' and are actions that can be executed when called


# what is contained in the parentheses is passed along into the function, in the example below we pass 2 which is then
# divided by 20
def myfunction(number):
    print(20/number)


mynumber = 2
myfunction(mynumber)


# classes create objects basically
class TestObject(object):
    # __init__ is run at the start of object creation and shows the data that must be passed
    def __init__(self,firstvar,secondvar):
        # create the values for the object using what was passed
        self.firstvar = firstvar
        self.secondvar = secondvar

    # Use self here because its using the info that exists in the object. In this case, it's what was passed in __init__
    def PrintValue(self):
        print(self.firstvar, self.secondvar)


# create an instance of the object and provide the initialization values
myobject = TestObject("test1", "test2")

# now I call the function of the object that prints the stored values
myobject.PrintValue()
