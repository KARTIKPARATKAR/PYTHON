#Sum of natural numbers
a=int(input("Give the starting number"))
b=int(input("Give the ending number"))
sum1=(a*(a+1))//2
print("Sum of starting:",sum1)
sum2=(b*(b+1))//2
print("Sum of ending:",sum2)
sum=sum2-sum1
print("Sum of numbers between ",a," and ",b," is",sum)
