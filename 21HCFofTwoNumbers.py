#Write code to find HCF of two numbers
def calhcf(x,y):
  if(x>y):                          #If x is greater then store y as smaller
    smaller=y
  else:
    smaller=x                       #If y is greater then store x is smaller
  for i in range(1,smaller+1):      #This will iterate through 1 to smaller+1
    if((x%i==0) and (y%i==0)):      #It will check after dividing whether both the numbers x and y gives 0 as remainder or not
      hcf=i
  return hcf
x=int(input("Give first number:"))
y=int(input("Give second number:"))
print("The hcf of ", x ,"and", y ," is :" ,calhcf(x,y))
