#Set
set={1,2,3,4,5,6,7,8,9}
for i in set:
    print(i)

stuid={11,22,33,44,55,66,77,88,99}
print("Student_Id is:",stuid)   #This will give unordered student id as set is unorered data structure

mixed={1,2,5.8,"Hello"}
print(mixed)



dupli={1,2,3,4,5,67,8,7,5,4,3,1,8}
print(dupli)    #This print will not print duplicate emenets in a set


num={12,23,34,56}
num.add(99)
print(num)  #This will add the element 99


test={"Apple","Orange","Banana","Watermelon"}
test.add("Stawberry")
print(test)
test.remove("Apple")
print("Set after removing apple is:",test)



names={"A","B","C","D"}
for name in names:
    print(name)
print(len(names))



A={1,1,2,3,4,5,6,7}
B={5,6,7,8,9,10}
print("Union of two sets A and B is:",A|B)  
print("Intersection of two sets A and B is:",A&B)
print("Difference of two sets A and B is:",A-B)
print("Difference of two sets B and A is:",B-A)
if A==B:
    print("Set A and B are equal")
else:
    print("Sets A and B are not equal")
