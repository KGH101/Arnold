# offers a concise way to create a new list from another list
# create a list of even numbers between 20 and number 100
even_numbers=[]
for i in range(20,101):
    if i%2==0:
        even_numbers.append(i)
print(even_numbers)

# or

even_numbers=[i for i in range(20,101) if i%2==0]
# for i in range(20,101):
    #if i%2==0:
        #even_numbers.append(i)
print(even_numbers)

# store in a list a square of numbers between 1 and 20

squares = [i ** 2 for i in range(1, 21)]
print(squares)

# or

squares = []  # Initialize an empty list

for num in range(1, 21):  # Loop through numbers from 1 to 20
    squares.append(num ** 2)  # Append the square of each number to the list

print(squares)