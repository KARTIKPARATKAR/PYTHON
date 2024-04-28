#String
x=input("Give first string:")   #When you take input from the user,it is in the string format by default
y=input("Give second string:")
if(x==y):           #This is checking whether both strings are same or not
  print("Strings are equal.")
t="aim" in x        #This is checking whether "aim" is in the string x or not
print("aim in the string x:",t)
p="hollow" in y     #THis is checking whether "hollow" is in the string y or not
print("hollow in the string y:",p)
print("Lower case first string is: ",x.lower())
print("Lower case second string is: ",y.lower())
