"""

Creating our own Datatype in Python

for eg - fraction 
python do not perform the fraction operation it gives the value in decimal


# Magic Methods

Are those special methods Jinko object call nahi krta ve apne aap automatically call ho jate h 

"""


class Fraction:
    
    def __init__(self, n, d):
        self.num = n 
        self.deno = d
        
        # print(self.num,"/",self.deno)
        # print(self.deno)
    def __str__(self):
        # this function returns the string 
        return "{}/{}".format(self.num,self.deno)

    def __add__(self,other):

        temp_num = self.num*other.deno + self.deno*other.num
        temp_deno = self.deno*other.deno
        
        return "{}/{}".format(temp_num,temp_deno)

    def __sub__(self,other):

        temp_num = self.num*other.deno - self.deno*other.num
        temp_deno = self.deno*other.deno
        
        return "{}/{}".format(temp_num,temp_deno)
    
    def __mul__(self,other):

        temp_num = self.num*other.num
        temp_deno = self.deno*other.deno
        
        return "{}/{}".format(temp_num,temp_deno)
    
    def __truediv__(self,other):

        temp_num = self.num * other.deno
        temp_deno = self.deno * other.num
        
        return "{}/{}".format(temp_num,temp_deno)
    
    # This function is some what wrong as how we will be able to calculate the rational ki power rational 
    # That's why it might become correct but for now this is wrong or i can say incomplete 

    # def __pow__(self,other):
    #     if(other == 0): return 1
    #     else:
    #         sum = 1
    #         while (other != 1):
    #             sum *=  self.num
    #             other-=1

    #     return "{}".format(sum)
    
    def __eq__(self,other):
        val1 = self.num / self.deno
        val2 = other.num / other.deno
        
        if (val1 == val2):
            print("Equal fractions")
        else:
            print("Not equal fractions")
    
    def __lt__(self,other):
        val1 = self.num / self.deno
        val2 = other.num / other.deno
        print(val1)
        print(val2)
        if (val1 < val2 ):
            print("True")
        else:
            print("False")
    
    def __ge__(self,other):
        val1 = self.num / self.deno
        val2 = other.num / other.deno
        if (val1 >= val2 ):
            print("True")
        else:
            print("False")
        
    def __le__(self,other):
        val1 = self.num / self.deno
        val2 = other.num / other.deno
        if (val1 <= val2 ):
            print("True")
        else:
            print("False")
        
    def __ne__(self,other):
        val1 = self.num / self.deno
        val2 = other.num / other.deno
        if (val1 != val2 ):
            print("True")
        else:
            print("False")
    
num = int(input("Enter the num "))
deno = int(input("Enter the deno"))
print("Stored in x object")
x = Fraction(num,deno)
# y = Fraction(3,4)
# z = Fraction(4,5)
# u = Fraction(1,1)
# v = Fraction(11,3)
