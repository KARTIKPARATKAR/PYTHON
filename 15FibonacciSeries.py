#Print Fibonaci series
# the Fibonacci sequence is a sequence in which each number is the sum of the two preceding ones.
t1=0
t2=1
num=int(input("Give the range till:"))
print(t1,",")
print(t2,",")
for i in range(0,num):
    t3=t2+t1
    print(t3)
    t1=t2
    t2=t3
