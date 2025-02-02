# Getting more about string

# Format
a = "Hello my name is {} and I am {}"
print(a.format("Prashant ",20))

b= "Hello my name is {1} and I am {0}"
print(b.format("PRashant",20))

c = "Hello my name is {name} and I am {age} year old."
print(c.format(name ="Prashant", age = 20))

c = "Hello my name is {age} and I am {name} year old."
print(c.format(name ="Prashant", age = 20))
# with the help of this we can use the values which are need for us.
# we can use only name on both place 
# get more details when we will make the projects

print("Fast250km".isalnum())
print("Fast250km%".isalnum())
print("Flat".isalpha())
print("Flat30".isalpha())
print("20".isdigit())
print("20a".isdigit())
print("hello world".isidentifier())
print("hello_world".isidentifier())

# there are various questioning functions which are used like that.

# split() = function makes a string into a list
print("Who is the current tech lead of Jugaad ?".split())
print("Who is the current tech lead of Jugaad ?".split("pm"))
print("Who is the current tech lead of Jugaad ?".split("e"))
print("Who is the current tech lead of Jugaad ?".split("x"))

# join = if we are having a list and we want to convert it into a string 
print(" ".join(['Who', 'is', 'the', 'current', 'tech', 'lead', 'of', 'Jugaad', '?']))
print("-".join(['Who', 'is', 'the', 'current', 'tech', 'lead', 'of', 'Jugaad', '?']))
print("e".join(['Who is th', ' curr', 'nt t', 'ch l', 'ad of Jugaad ?']))

# replace = used for replacing the data of a specific value.
print("Prshant Choudhary is the tech lead".replace("Prshant Choudhary","Nikhil Mishra"))

# strip = used to remove the space before and after the word/data

name = "        prashant        " 
print("Hello,",name," is here")
print("Hello,",name.strip(),"is here")