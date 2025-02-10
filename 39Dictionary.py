#Dictionary
dictionary={}
print(dictionary)

dict={"Name":"Karan","Age":25,"Class":12}
print(dict)
print("Age is:",dict["Age"])


dict={}
dict["Age"]=25
dict["Name"]="Virat"
dict["Home"]="Delhi"
print(dict)


test={"1":"One","2":"Two","3":"Three"}
print(test)
test.popitem()  #This will pop key-value pair from dictionary
print(test)

#For loop in dictionary
t={"Player":"Virat","Runs":25,"Ground":"Pune","Coach":"Gambhir"}
for key_value in t.items():   #Here t.items() returns all key-value pairs from the dictionary as tuples
    print({key_value})

for k,v in t.items():
    print((k,v))

num={"One":1,"Two":2,"Three":3,"Four":4}
print(num["One"])
