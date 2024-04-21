#Printing all prime number in a given range
n1=int(input("Give start of range:"))
n2=int(input("Give end of the range:"))
for num in range(n1,n2+1):  #Here num is iterating through the range n1 to n2+1
  if(num>1):                #Ensuring that the num is greater than 1
   flag=True                #Declaring flag as true intially
   for i in range(2,num):   #Here i will iterate from 2 to num
     if(num%i==0):          #Checking whether the number is divisible by any numbers between 2 to num
      flag=False            #If divisible then making flag as false
      break                 #Breaking the current iteration
   if(flag):                #Here if flag is true then print the number as prime number
      print(num)
  
