#Write a code to find the number of strings in a list having length more than 2 and the 1st and the last character are same.
n=int(input("Give the number of strings to be stored in a list:"))
mylist=[]
for i in range(n):
  x=input()
  mylist.append(x)               #Appending the string given by user in the list
print("Your created list is:",mylist)
words=0                          #Defining words=0 to count the required number of words
for string in mylist:            #For every string in the list called mylist
  if(len(string)>1 and string[0]==string[-1]):    #This will check length of the string is greater than 1 or not and 1st and last character in a string are same or not.
    words=words+1                                 #If conditioon satisfiesthen we will add 1 to the words
print("Total number of words are:",words)
