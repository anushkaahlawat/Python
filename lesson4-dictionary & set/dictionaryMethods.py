#1. myDict.keys()  method                           # returns all keys


'''student = {

    "name"   :   "Anushka",
    "age"    :   18,
    "marks"  : {
        "chem" : 89,
        "phys" : 75,
        "maths": 80
    },
    "favColor" : ("maroon","pink","blue","black","yellow","red"),
}


student["name"] = "Anushka Ahlawat"
student["favColor"] = ("maroon","pink","blue","yellow","red","black","white")
print(student)

print(student.keys())
print(len(student))'''



# 2. myDict.values()  method                         # returns all values 



"""dict = {
    "name" : "anushka",
    "age"  :   18,
    "favColor" : "maroon",
    "marks"   : 9.00,
    "value" : [12,34,5,6,78,98],
    "more"  : ("White","yellow","blue","black"),
    "fullName" : "Anushka ahlawat"
    }

print(type(dict))
print(dict["name"])
print(dict["value"])
print(dict["more"])
print(dict["fullName"])

print(list(dict.values()))
print(len(dict))"""




# 3. myDict.items()  method                          # returns all (key,value) pairs as tuples 




'''std = {

    "name"   :   "Anushka",
    "age"    :   18,
    "marks"  : {
        "chem" : 89,
        "phys" : 75,
        "maths": 80
    }
}

print(std)
print(len(std))

print(list(std.items()))'''




# 4. myDict.get("keys")  method                      # returns the key according to the value




'''dictionary = {
    "name" : "anushka",
    "age"  :   18,
    "favColor" : "maroon",
    "marks"   : 9.00,
    "value" : [12,34,5,6,78,98]
    }

print(dictionary)

print(list(dictionary.get("value")))
print(list(dictionary.get("name")))
print(list(dictionary.get("favColor")))'''




# 5. myDict.update(newDict)  method                  # inserts the specified items to the dictionary 



dict = {
    "name" : "anushka",
    "age"  :   18,
    "favColor" : "maroon",
    "marks"   : 9.00,
    "value" : [12,34,5,6,78,98]
}


dict.update({"city" : "Meerut"})
dict.update({"name" : "Anushka ahlawat"})
print(dict)

