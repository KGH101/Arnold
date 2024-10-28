# trainees = ["John", [2, ["James","Mary"]]]

# Display 2 from the list.
trainees = ["John", [2, ["James","Mary"]]]
n = trainees[1][0]
print(n)

# Output James from the list.
trainees = ["John", [2, ["James","Mary"]]]
j= trainees[1][1][0]
print(j)


# Using a method add 56 at the end of the list.
trainees = ["John", [2, ["James","Mary"]]]
trainees.append(56)
print(trainees)

# Using a method add the name Mike between James and Mary
trainees = ["John", [2, ["James","Mary"]]]
trainees[1][1].insert(1,"Mike")
print(trainees)

# Change the value of 2 to 8
trainees = ["John", [2, ["James","Mary"]]]
trainees[1][0]=8
print(trainees)

# Remove John and Mary from the list.
trainees = ["John", [2, ["James","Mary"]]]
trainees.remove("John")
trainees[0][1].remove('Mary')
print(trainees)


# Using a function, determine the length of the list
trainees = ["John", [2, ["James","Mary"]]]
t= len(trainees)
print(t)