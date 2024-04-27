#Write a program to multiply all the elements in a list
n=int(input("Give number of elements in list:"))
mylist=[]
for i in range(1,n+1):
  x=float(input())    #This is taking integer input from the user
  mylist.append(x)    #This is appending the user input value in mylist
print("Your created list is:",mylist)
mul=1
for i in range(n):
  mul=mul*mylist[i]   #Multiplying all the list elements and storing it in mul
print("Multiplication of list elements are:",mul)
