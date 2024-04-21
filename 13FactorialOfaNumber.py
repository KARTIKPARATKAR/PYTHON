num=int(input("Give the number:"))
fact=1
for i in range(num,0,-1):   # i is iterating in the range of num to 0(excluding) decrementing the value by 1 in each iteration
    fact*=i                 #multiplying factorial by i in each iteration
print("Factorial is:",fact)
    
