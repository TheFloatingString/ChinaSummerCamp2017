import math
from math import pi

"""
This is a multiline comment
"""

def execute_example_code():
    # Print statement
    print("Hello world!\n\n")

    # Variables
    random_variable =  10
    random_string = "This is a STRING"

    choice = input("ENTER 1 IF YOU WANT TO SKIP DIRECTLY TO THE OBJECT ORIENTED PROGRAMMING: ")
    if choice == '1':
        pass
    else:
        # if /else statement
        if random_variable == 10 or random_variable==20:
            print(random_variable)
        else:
            print("FALSE")

        for i in range(10):
            print(i)

        while random_variable < 20:
            print(random_variable)
            random_variable = random_variable + 1

        anInt = 0

        def printString(anInt):
            print(anInt*2)
            anInt2 = anInt*2
            return anInt2

        varRand = printString(20)
        print(varRand)

        var0 = 0

        # Error handling with python

        try:
            print(0/0)
        except:
            print("error!")

        print(math.pi)
        print("\n\n\n\n")

class Pillow:
    """Parent class"""
    def __init__(self,comfy,squishy):
        self.comfy = comfy
        self.squishy = squishy

    def printPillow(self):
        print("COMFORT {}".format(self.comfy))
        print("SQUISHY {}".format(self.squishy))

    def measureComfort(self):
        if self.comfy > 10 and self.squishy > 5:
            print("THIS IS A SUPER COMFY PILLOW!!!")
        else:
            print("THIS IS NOT A COMFY PILLOW!!!")

class DUTCH_GUY(Pillow):
    """Child class"""
    def __init__(self,comfy,squishy,isCool,isSmart):
        super().__init__(comfy, squishy)   # Initialize parent class instance
        self.__isCool = __isCool           # Private attribute
        self.isSmart = isSmart

    def isACoolDutchGuy(self):
        if self.__isCool >5 and self.isSmart > 5:
            print("THIS IS A COOL DUTCH GUY")
        elif self.__isCool >3 and self.isSmart>2:
            pritn("THIS GUY IS DUTCH")
        else:
            print("NOT DUTCH")


if __name__ == "__main__":
    execute_example_code()

    # Object oriented programming
    Kelvin = DUTCH_GUY(10,0,10,9)
    Kelvin.printPillow()
    Kelvin.measureComfort()
    Kelvin.isACoolDutchGuy()
