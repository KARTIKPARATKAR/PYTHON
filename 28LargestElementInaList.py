#Write a program to get the largest numbrer from list
n=int(input("Give the number of integers in list:"))
mylist=[]
for i in range(n):
  x=int(input())
  mylist.append(x)
print(mylist)
largest=mylist[0]
for i in range(n):
  if(mylist[i]>largest):
    largest=mylist[i]
print("The largest element is ",largest)
