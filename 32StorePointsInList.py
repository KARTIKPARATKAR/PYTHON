#Write a program to store the co-ordinates of a points in a list
n=int(input("How many points do you want to strore?:"))
points=[]                           #This is a empty list of points
for i in range(n):
  x=int(input("Give abscissa :"))
  y=int(input("Give ordinate :"))
  points.append((x,y))             #Appending ordered pair of (x,y) in a list
print("Your created list of points are:",points)    #Printing the created list of points
