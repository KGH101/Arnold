person={"name":"Arnold",
        "age":25,
        "gender":"Male",
        "location": ["kiambu", 518,"Thika"],
        "address":{
            "street":"muthaiga",
            "city":"Nairobi",
            "country":"Kenya"
            }
        
        }


print(type(person))
print(person["name"])

# unordered
# accessing values by reffering to their keys
# age
print(person["age"])

# gender

print(person["gender"])

# 518

print(person["location"][1])

# Thika

print(person["location"][2])

# Street

print(person["address"]["street"])

# City

print(person["address"]["city"])


# updating values
person["age"]=40
print(person)

person["location"]= "Kericho"
print(person)

# Add new key and a value

person["occupation"]= "Doctor"
print(person)


# dictionary methods
# .keys = returns all the keys in the dictionary

print(person.keys())
# .values = returns all the values in the dictionary

print(person.values())
# .items = returns a list of key and value

print(person.items())

# pop = removes value belonging to a specified key

person.pop("name")
print(person)

#remove occupation

person.pop("occupation")
print(person)

# get () returns the value of a specified key

print(person.get("address"))

