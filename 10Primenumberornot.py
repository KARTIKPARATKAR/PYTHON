#Write code for finding number is prime or not
num=int(input("Give number:"))
is_prime=True;
for i in range(2,num):   #Here range function has two arguments i.e. 2 and num which means that the value of i will iterate from 2 to num and excluding num.
  if(num%i==0):
    is_prime=False;
if(is_prime and num>1):
  print(num," is a prime number.")
else:
  print(num," is not prime number.")
