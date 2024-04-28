#Write a code to find the 1st and last character of a string
print("Give your string:")
s=input()
l=len(s)
print("Your string is:",s)
print("Length of string is:",l)
print("First character of string is:",s[0])
print("Last character of string using negative indexing is:",s[-1])  #Negative indexing allows user to access the elements in a string from the end. NOrmal indexing strats from 0 at start and negative indexing starts from end with -1.
print("Last character of string using length of string is:",s[l-1])  
#So at index -1 , we get the last character of the string in reverse indexing
