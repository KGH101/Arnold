# Write a program that displays a numbers 1 to 50 inside a list.

numbers = list(range(1,51))
print(numbers)



# From 1 above display the ones divisible by 7 or 5 inside a list.

divisible_seven_5=[]
for i in numbers:
    if i%7==0 or i%5==0:
        divisible_seven_5.append(i)


print(divisible_seven_5)

# Find sum and average of values in the range between 10 to 40.

numbers = list(range(10,41))
sum=0
count=0

for i in numbers:
    sum+=i
average=sum / len(numbers)    
print(sum)    
print(average)
#total_sum = sum(numbers)
#average = total_sum / len(numbers)

#print(f"Sum: {total_sum}")
#print(f"Average: {average}")#


# Put in a list the first 10 odd numbers between 10 to 50.


numbers = list(range(10,50))
odd=[]
for i in numbers:
    if i%2!=0:
        odd.append(i)
    if len(odd)==10:
        break
print(odd)   

    # or

numbers = list(range(10,50))
odd=[]   
count=0

for i in numbers:
    if i%2!=0:
        odd.append(i)
        count+=1
        if count==10:
            break

print(odd)
    



# write a program that takes a number as input and prints its
# multiplication table up to 10 using a for loop.

number = int(input("Enter a number: "))
for i in range(0, 11):
    mult=number*i
    print(f"{number} x {i} = {mult}")


# write a program that counts and prints the number of even numbers
# between 1 and 50 using a for loop

count_even = 0

# Loop through numbers from 1 to 50
for i in range(1, 51):
    # Check if the number is even
    if i % 2 == 0:
        count_even += 1

# Print the total count of even numbers
print(f"The number of even numbers between 1 and 50 is: {count_even}", count_even)


# ls1 = [ (“Jay”, 20), (“Mo”, 30), (“Mya”, 32) ]
# Display the total quantity of the 3 above.


ls1 = [("Jay", 20), ("Mo", 30), ("Mya", 32)]

total_quantity = 0


for i in ls1:
    stock=i[1]
    total_quantity = total_quantity + stock # total_quantity += item[1]

print(f"Total Quantity: {total_quantity}", )