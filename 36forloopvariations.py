my_list=[1,2,3,4,5,6,7]
for i in my_list:
    print(i)



numbers=[1,2,3,4,5,6,7,8,9]
for i in numbers:
    print(i)
    if(i==5):
        break 




my_list=[1,2,3,4,5,6,7,8,9]
for i in my_list:
    print(i)
    if(i==6):
        print("Loop is break when i=",i)
        break



num=[1,2,3,4,5,6,7,8,9,10]
for i in num:
    if(i%2==0):
        print(i,"is divisible by 2")




list=[1,2,3,4,5,6,7,8,9,10]
for i in list:
    if(i%2==0):
        continue
    else:
        print(i,"is not divisible by 2")



for i in range(1,10):  #This is range from 1 to 9 so it will print 1 to 9 only.
    print(i)



for i in range(1,10,2):  #Range stars from 1 goes till 10 with increment of 2
    print(i)




mylist=[24,75,2,56,87,45]
for i in mylist:
    if(i%7==0):
        print(i," is a multiple of 7")
        continue                        #This continue will skip the current iteration and jumps to next iteration
    else:
        print(i," is not a multiple of 7")
