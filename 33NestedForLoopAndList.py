#Nested loops
for i in range(10):     #THis code will create a rectangle of 10 rows and 5 columns having symbol *
  for j in range(5):
    print("*",end=" ")
  print()

--------------------------------------------------------------------------------------------------------------------------------------------------------------


mylist=[]              
for i in range(5):       #Nested for loop. Outer loop value i takes from 0 to 4
  for j in range(3):     #Inner loop value j takes from 0 to 2
    mylist.append([i,j])  #appending values of i and j in the mylist as a order
print(mylist)             #Printing the mylist
