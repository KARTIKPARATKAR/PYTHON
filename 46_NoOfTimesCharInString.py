#Counting number of occurance of a character in a string
char = 'a'
string = 'Programming'
count=0
for i in string:
    if i == char:
        count=count+1
print("Occurance of ",char,"is ",count," times")
