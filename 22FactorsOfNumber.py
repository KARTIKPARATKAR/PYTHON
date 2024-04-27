#Find the factors of a number given by the user
x=int(input("Give the number:"))
print("The factors of ",x," are:")
for i in range(1,x+1):    #This for loop will iterate from 1 to x value given by the user to check whether the remainder after dividing is 0 or not
  if(x%i==0):             #If remainder is 0 then it is a factor of that number
    print(i)
