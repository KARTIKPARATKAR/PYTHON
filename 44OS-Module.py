#When os is imported, it lets the user interact with the native OS Python is currently running on.
import os
print(os.name)  #Prints os name
#os.mkdir("data")  #This will create a directory having name data
print(os.getcwd())  #This will print the current working directory

os.rmdir("data") #This will remove the directory name "data"
