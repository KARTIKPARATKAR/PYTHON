#ax**2+bx+c
#Followinfg is the roots found out by importing cmath library
import cmath
a=int(input("Give a (a!=0):"))
b=int(input("Give b:"))
c=int(input("Give c:"))
det=b**2-4*a*c
r1=(-b+cmath.sqrt(det))/(2*a)
r2=(-b-cmath.sqrt(det))/(2*a)
print("Root 1 is ",r1," and root 2 is ",r2)

#Following is the roots of quadratic equation found out without importing cmath library
a=float(input("Give a:\n"))
b=float(input("Give b:\n"))
c=float(input("Give c:\n"))
det=b**2-4*a*c
r1=(-b+(det)**0.5)/2*a
r2=(-b-(det)**0.5)/2*a
print("Root r1 is:",r1," and r2 is:",r2)
