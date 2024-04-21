#THis is method 1 using the formula of finding the sum of first n natural numbers.
#Sum of natural numbers
a=int(input("Give the starting number"))
b=int(input("Give the ending number"))
sum1=(a*(a+1))//2
print("Sum of starting:",sum1)
sum2=(b*(b+1))//2
print("Sum of ending:",sum2)
sum=sum2-sum1
print("Sum of numbers between ",a," and ",b," is",sum)


#This is a method using the for loop which iterate through the given range and add all the numbers in variable sum to get the desired sum
#Sum of natural numbers
a=int(input("Give the starting number"))
b=int(input("Give the ending number"))
sum=0
for i in range(a,b):
    sum=sum+i
print("The sum between ",a," and ",b," is ",sum)
