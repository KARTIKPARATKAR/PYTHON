#swap two numbers without using 3rd variable
a=int(input("Give 1st number:"))
b=int(input("Give 2nt number:"))
print("1st and 2nd number before swapping is ",a," ",b)
a=a+b
b=a-b
a=a-b
print("1st and 2nd number after swapping is ",a," ",b)
