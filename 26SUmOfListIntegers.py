#Write a program to add the all elements in a list
n=int(input("Give how many values are there in a list:"))
mylist=[]
for i in range(1,n+1):
  x=float(input())
  mylist.append(x)
print("Your Created list is:",mylist)
sum=0
for i in range(n):  #Here n is the length of the list
  sum=sum+mylist[i]
print("The sum of list elements is:",sum)
