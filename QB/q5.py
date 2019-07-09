"""Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods."""
class Inputstring:

    def __init__(self):
        self.s = ""

    def getstring(self):
        self.s = input()

    def putstring(self):
        print(self.s.upper())

Obj = Inputstring()
Obj.getstring()
Obj.putstring()