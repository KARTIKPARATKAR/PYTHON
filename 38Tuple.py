#tuple
tuple=()
print(tuple)

num=(1,2,3,4,5,6)
print(num)


mixed=(1,"Hello",0.5,True)
print(mixed)

nested_tuple=("Python",5,[2,1,3,4,],25.5)
print(nested_tuple)

val=100,"hello",5.9
print(val)


test=(5,)   #If u are creating tuple of one element,comma is necessary to tell that it is tuple
print(type(test))

my_tuple=("Hello","World",1,4,9.1,True)
print("Element at 0th index:",my_tuple[0])
print("Element at 3rd index:",my_tuple[3])
print("Element at -1 index is:",my_tuple[-1])
print("Tuple slicing with index 0 to 1:",my_tuple[:2])


mytuple=(1,2,4,6,4,21,4,5,8,4,2,4,2,1,3,2,5,3)
print("2 is occured",mytuple.count(2),"times")
print("4 is occured",mytuple.count(4),"times")



a=(1,2,3,4,5,6,7,10)
b=(4,5,6,7,8,9,10)
print("Length of tuple a is:",len(a))
print("Length of tuple b is:",len(b))
print("Max of a is:",max(a))
print("Max of b is:",max(b))
print("Min of a is:",min(a))
print("Min of b is:",min(b))
print(1 in a)
print(4 in b)
print(9 in a)


c=("Karan","Kabir","Kishan")
for i in c:
    print(i)
