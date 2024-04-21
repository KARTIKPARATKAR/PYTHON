#Find numbers in range which is divisible by another number
num=int(input("GIve the number:"))
start=int(input("Give the strting range:"))
end=int(input("Give the ending range:"))
for i in range(start,end):
    if(i%num==0):
        print(i," is divisible by ",num)


