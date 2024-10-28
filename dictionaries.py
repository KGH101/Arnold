# its used to store related data in form of key value

# key will always be a string
# key is always unique
# value can be any datatype
person={"name":"arnold",
        "age":25,
        "location":"utawala"}

# unordered
# accessing values by reffering to their keys
print(person["location"])

# adding values to a dictionary

person={"name":"arnold",
        "age":25,
        "location":"utawala"}
person["occ"]="doctor"
print(person)

# add 
details={
    "name": "josh",
    "class": "4N",
    "ADM": 5496,
    "addr": {
        "code": 20200,
        "street":"kimathi"
    },
    "subjects": ["eng","ksw","comp"],
    "results":("a","b")
}

# add town to addr
details["addr"]="town"
print(details)

# add chemistry to subjects

details['subjects'].append('chemistry')
print(details['subjects'])


#remove
del details["results"]
print(details)
details["subjects"].remove("ksw")
print(details)


# dictionary methods

person={"name":"arnold",
        "age":25,
        "location":"utawala"}

# keys- returns only the keys
print(person.keys())

# values - returns all the values
print(person.values())

# items - returns all the key-value pairs
print(person.items())

# clear
# copy
# update 




















# Create a file called mydstask.py and attempt the below questions:
#my_ds = [23, “Jane”, (560), [“Lesson”, “Maths”, {“currency” : “KES”}], 987,
#(76,”John”)]

 # Print KES
my_ds = [23, "Jane", (560), ["Lesson", "Maths", {"currency" : "KES"}], 987,
(76,"John")]

# Print KES

print(my_ds[3][2]["currency"])

 # Print 560 
print(my_ds[2])

 # Print Maths
print(my_ds[3][1])

 # In the dictionary with the key currency, add another key “amount” with value 90
my_ds[3][2]["amount"] = 99
print(my_ds)

 # Reverse 987 to 789 without using an inbuilt -method or Assigning 789 manually.
my_ds = [23, "Jane", (560), ["Lesson", "Maths", {"currency" : "KES"}], 987,
(76,"John")]

x = str(my_ds[4])[::-1]
my_ds[4] = int(x)
print(my_ds)

# Hint: Strings can be reversed using [::]


# Change the name “John” to “Jane” .
y= list(my_ds[5])
y[1]= "jane"
my_ds
print(y)
