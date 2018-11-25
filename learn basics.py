import numpy 
import matplotlib.pyplot 




# this is the first comment
spam = 1  # and this is the second comment
          # ... and now a third!
text = "# This is not a comment because it's inside quotes."

#The interpreter acts as a simple calculator:
#you can type an expression at it and it will write the value.
#Expression syntax is straightforward: the operators +, -, * and / work just like in most other languages
#parentheses (()) can be used for grouping.

#>>> 2 + 2
#4
#>>> 50 - 5*6
#20
#>>> (50 - 5*6) / 4
#5.0
#>>> 8 / 5  # division always returns a floating point number
#1.6
condition = 1

while condition <= 10 :
    print('The counter is :',condition)

    condition+=1

print(str(5))
print(float(8))
print(int(8))
print(int('8')+float('8.5'))    

print('We\'re heros')
print("We're heros")
#declare packegr
x,y = 3,5
print('x',x,'y',y)
#swap variables
x,y=y,x
print('x',x,'y',y)
mylist =list( range(10) ) 
print(mylist)

#for loop
for n in range(10): 
    #print(n) 
    print("The square of", n, "is", n*n) 
    pass
print("done")
# range(10) creates a list of numbers from 0 to 9
# The “pass” instruction signals the end of the loop

# the following prints out the cube of 2 
print(2**3) 
# ** = ^ (power to)

# function that takes 2 numbers as input 
# and outputs their average 
def avg(x,y): 
    print("first input is", x) 
    print("second input is", y)  
    a = (x + y) / 2
    #a = (x + y) / 2.0 the same here 
    print("average is", a) 
    return a 

avg(200,301)

#  use arrays to represent the matrices

a = numpy.zeros( [3,2] ) 
print(a) 

#  you can refer to specific cells to overwrite them with new values

a[0,0] = 1 
a[0,1] = 2 
a[1,0] = 9 
a[2,1] = 12 
print(a) 

print(a[0,1]) 
v = a[1,0] 
print(v) 

matplotlib.pyplot.imshow(a, interpolation="nearest")

# the difference between classes​ ​
# and ​ objects​ , one is a definition and one is a real instance of that definition
# A class is a cake recipe in a book, an object is a cake made with that recipe.

# class for a dog object 
class dog : 
    def __init__(self,petName,temp):
        self.temperature = temp
        self.name = petName

    # dogs can bark() 
    def bark(self): 
        print("woof!") 
        pass
    pass 

    def setTemp(self,temp):
        self.temperature =temp

    def status(self):
        print("My name is",self.name,"My temperature is",self.temperature)

sizzles = dog("sizzles",35)
mutley = dog("mutley",40) 
mutley.bark()
sizzles.bark()
sizzles.status
mutley.setTemp(45)  
mutley.status()



