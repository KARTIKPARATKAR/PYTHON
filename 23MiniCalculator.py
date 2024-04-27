#Construct a mini calculator
x=int(input("Give 1st value:"))
y=int(input("Give 2nd value:"))
choice=int(input("Press 1 for addition \n Press 2 for subtraction \n Press 3 for multiplication \n Press 4 for division \n Press 5 for remainder \n"))  #Here \n takes the printing in next line
if choice==1:
  print(x+y)
elif choice==2:
  print(x-y)
elif choice==3:
  print(x*y)
elif choice==4:
  print(x/y)
elif choice==5:
  print(x%y)
