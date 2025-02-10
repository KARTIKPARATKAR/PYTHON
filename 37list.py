#Python list

#Printing the list
fruits=["Banana","Apple","Orange"]
for i in fruits:
    print(i)



mylist=[1,2,3,4,5,6,7]
print("Original list is:")
print("Element at 0th index before removing 1 is:",mylist[0])
for i in mylist:
    print(i)
print("Removing 1 from mylist:")
mylist.remove(1)
print("Printing list after removing 1:")
for i in mylist:
    print(i)
print("Element at 0th index before removing 1 is:",mylist[0])



#Slicing the list
list=[1,2,3,4,5,6,7,8,9]
print(list)  #This will print whole list
print(list[0:3]) #This will print the list from 0th index to 2nd index because 3 is excluded here
print("Removing 5 in list:")
list.remove(5)
print(list)



collection=[4,7,2,6,9,4,1,5,8,1,7,6,3,9]
print("Printing the original list:")
for i in collection:
    print(i)
print("Appending 100 in collection:")
collection.append(100)
print("Printing the collection list after appending 100:")
for i in collection:
    print(i)
print("Removing 8 from the collection:")
collection.remove(8)
print("Printing the collection after removing 8:")
for i in collection:
    print(i)
print("Now using pop function on collection:")
collection.pop()
print("Printing the collection after using pop function:")
for i in collection:
    print(i)
collection.sort()
print("Colection after sorting function used:")
for i in collection:
    print(i)
collection.reverse()
print("Collection after using reverse function:")
for i in collection:
    print(i)



print("Creating a empty list empty_list[]")
empty_list=[]
print(empty_list)
print("Adding elemtns in a list:")
empty_list.append("Cricket")
empty_list.append("Tennis")
empty_list.append("Base-Ball")
print("Printing the empty list after appending 3 sports:")
for i in empty_list:
    print(i)


#Taking userinput to create a list
mylist=[]
a=int(input("How many elements in a list?"))
print("Give ",a,"input elements in a list")
for i in range(0,a):
    x=int(input())
    mylist.append(x)


#Accessing the list element by index
list=[]
a=int(input("No of ements in a list:\n"))
for i in range(0,a):
    x=int(input())
    list.append(x)
print("List created is:\n")
for i in range(0,a):
    print(i)
print("Element at index 2 is:",list[2])
print("Element at index 3 is:",list[3])
print("Element at index -1 is:",list[-1])  #This means last element



#Slicing the list and storing it in another list
mylist=[]
a=int(input("Give no of elements in a list:\n"))
for i in range(0,a):
    x=int(input())
    mylist.append(x)
print("List created is:\n",mylist)
slice=mylist[0:3]  #This will create a new list "slice" with index elements from 0 to 2
print(slice)


#Insert
list=[0,2,3,4,6,8]
list.insert(1,5)  # Here inserting 5 at index 1
print(list)


#List concatenation
num=[1,2,3,4,5]
morenum=[6,7,8,9]
num=num+morenum  #Concatenate lists num and morenum and store it in another list num
print(num)


#Modifying a list element
list=[1,2,3,4,5,6]
print("Modifying element at index 2 and storing 100:\n")
list[2]=100
print(list)



#Replace the element with 0 if it is divisible by 10
list=[1,5,10,3,5,8,10,50,40,20]
print("Length of list is:",len(list))
for i in range(len(list)):
    if(list[i]%10==0):
        list[i]=0
print(list)


#Iterating in a list
list=[1,2,3,4,5,6,7,8,9,10]
for i in range(len(list)):
    print(list[i])

for i in list:
    print(i)

i=0
while i<len(list):
    print(list[i])
    i=i+1
