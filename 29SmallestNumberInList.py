#Write a program to get the smallest numbrer from list
n=int(input("Give the number of integers in list:"))
mylist=[]
for i in range(n):
  x=int(input())
  mylist.append(x)
print(mylist)
smallest=mylist[0]
for i in range(n):
  if(mylist[i]<smallest):
    smallest=mylist[i]
print("The smallest element is ",smallest)
