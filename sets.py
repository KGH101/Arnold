# collection of unique, unordered data
# enclosed with {}
# creating sets
my_set = {1,2,3,4,5,6,6}
print(my_set)

# use set function to convert data structures into set
# adding elements
my_set.add(7)
print(my_set)

#remove
my_set.remove(5)
print(my_set)


# membership(in)

print(6 in my_set)

# union= combine all elements from both sets
x= {"a","b","c"}
y= {"d","e","f"}

z= x.union(y)
print(z)

# intersection = returns elements common in both sets
a= {10,11,12,13}
b= {14,15,16,16,10,11,12,13}
c= a.intersection(b)
print(c)

#difference = returns elements in the first set but not in the second
a= {10,11,12,13,30,31,32,33}
b= {14,15,16,16,10,11,12,13,30,31}
c= b.difference(a)
print(c)

# symetric difference returns elements in either sets that are not in both
d= {1,2,3,4,5}
e= {4,5,6,7,8,9}
f= d.symmetric_difference(e)
print(f)


days = {"monday","tuesday","wednesday","thursday",
"friday","saturday","sunday","sunday","sunday","sunday"}
print(days)
# Remove friday and sunday from the set using methods.
days = {"monday","tuesday","wednesday","thursday",
"friday","saturday","sunday","sunday","sunday","sunday"}

days.remove("friday")
days.remove("sunday")
print(days)

#Add them back to the set



