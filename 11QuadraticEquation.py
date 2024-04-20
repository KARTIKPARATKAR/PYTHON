#ax**2+bx+c
import cmath
a=int(input("Give a (a!=0):"))
b=int(input("Give b:"))
c=int(input("Give c:"))
det=b**2-4*a*c
r1=(-b+cmath.sqrt(det))/(2*a)
r2=(-b-cmath.sqrt(det))/(2*a)
print("Root 1 is ",r1," and root 2 is ",r2)
