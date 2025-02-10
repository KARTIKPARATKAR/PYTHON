# Functions
def myfunction():                               #This is a basic function
    print("Printing from custome function")
myfunction()



def func(name):                                    #Function with parameter
    print("Name is:",name)
func("Kartik")



def add(a,b):                                      #Function with return value
    return a+b
p=add(4,5)
print(p)



def add():
    a=int(input())
    b=int(input())
    c=a+b
    return c
print(add())




glo_var=10
def test():
    loc_var=5
    print(glo_var+loc_var)
test()


#Lambda function
func=lambda a,b:a+b
print(func(4,3))


def add(a,b):
    c=a+b
    return c
d=add(4,5)
print(d)



import math
print("Square root of 4 is:",math.sqrt(4))
print("2 power 3 is:",pow(2,3))
