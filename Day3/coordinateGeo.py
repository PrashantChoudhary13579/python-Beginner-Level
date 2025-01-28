# Making a class of coordinate Geometry and making several methods to perform various operations 

import decimal

class coordinate:
    def __init__(self,x,y):
        self.__num1 = x
        self.__num2 = y
    
    def slope(self,other):
        self.sl = (other.__num2 - self.num2)/(other.num1 - self.num1)

        return "{}".format(self.sl)
    
    
    def square(self,num):
        return self.num*self.num
    
    def sqrt(x):
        return x ** .5
        """
        if x < 0 : print("Error")
        a = 1
        b = x
        while(abs(a-b)>ErrorMargin):
            a = (a+b)/2
            b = x/a
        return a """
    
    def distance(self,other):
        b = self.num2 - other.num2
        a = self.num1 - other.num1
        print(self.square(a))
        print(self.square(b))
        self.dist = sqrt(square(b) + square(a))

        return "{}".format(self.dist)


A = coordinate(6,4)
B = coordinate(5,2)
