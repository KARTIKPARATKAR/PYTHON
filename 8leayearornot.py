#Write program to check whether a given year is leap or not
y=int(input("GIve the year:"))
if(y%4==0):
  if(y%100==0):
    if(y%400==0):
      print("It is a leap year.")
    else:
      print("Not a leap year")
  else:
    print("It is a leap year.")
else:
  print("Not a leap year.")
