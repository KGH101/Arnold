fruits= ["mango",[1,2,3,4,5],"banana",100,30.5,False,True]

print(type(fruits))

# Accessing elements in a list
print(fruits[2])
print(fruits[5])
print(fruits[1][4])

# modifying elements in a list
fruits[0]="watermelon"
print(fruits)


# list methods
# append =  used to add elements at the end of a list

fruits.append("oranges")
print(fruits)

# insert = add items to a specific index

fruits.insert(1,1000)
print(fruits)

# remove = remove first occurence of a specific element
num= [10,20,30,40,50,10]
num.remove(10)
print(num)

# pop = removes item of a specific index 

num.pop(0)
print(num)

# slicing
print(num[0:3])


# len()= get length
print(len(num))

# check if an element is inside a list

students= ["maina","arnold","frank","vera","abdi"]
print("maina" in students)
print("anthony" in students)

# concatenate list

lst1=[1,2,3,4,5]
lst2=[6,7,8,9,10]
lst3=lst1+lst2
lst3=lst1+lst2
print(lst3)