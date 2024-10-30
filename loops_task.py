# Write a program that displays a numbers 1 to 50 inside a list.

numbers = list(range(1,51))
print(numbers)



# From 1 above display the ones divisible by 7 or 5 inside a list.

numbers = list(range(1,51))
for i in numbers:
    if i%7==0 or i%5==0:
        print(i)

# Find sum and average of values in the range between 10 to 40.

numbers = list(range(10,41))
total_sum = sum(numbers)
average = total_sum / len(numbers)

print(f"Sum: {total_sum}")
print(f"Average: {average}")


# Put in a list the first 10 odd numbers between 10 to 50.


numbers = range(10,51)
odd=[]
for i in numbers:
    if i%2!=0:
        odd.append(i)
    if len(odd)==10:
        break
    print(odd)    


# write a program that takes a number as input and prints its
# multiplication table up to 10 using a for loop.

number = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


# write a program that counts and prints the number of even numbers
# between 1 and 50 using a for loop


# ls1 = [ (“Jay”, 20), (“Mo”, 30), (“Mya”, 32) ]
# Display the total quantity of the 3 above.


s1 = [("Jay", 20), ("Mo", 30), ("Mya", 32)]

# Calculate the total quantity
total_quantity = sum(quantity for name, quantity in s1)

# Display the total quantity
print("Total quantity:", total_quantity)