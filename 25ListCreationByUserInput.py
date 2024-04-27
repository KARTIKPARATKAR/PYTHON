#Write a program to create a list of integers given by the user
n=int(input("Give the number of integers in a list:"))  #HEre give the number of integers in a list
mylist=[]                                               #Here create an empty list
for i in range(1,n+1):                                  #Here iterate for loop from 1 to n that is n times
  x=int(input())                                        #Taking input from user and storing it in a variable called x
  mylist.append(x)                                      #Appending that x integer in the list called mylist
print(mylist)                                          #Printing the list created
