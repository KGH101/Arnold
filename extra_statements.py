# 1.Assume start_date = '2024-01-01' and end_date = '2024-12-31'. Write a conditional statement that checks:
# If start_date comes before end_date, print "Valid period",
# If start_date is after end_date, print "Invalid period".
# If both dates are the same, print "One-day period".



start_date = '2024-01-01'
end_date = '2024-12-31'


if start_date < end_date:
    print("Valid period")
elif start_date > end_date:
    print("Invalid period")
else:
    print("One-day period")

# 2.Given two strings str1 and str2, write a conditional statement that checks:
# If str1 is longer than str2, print "str1 is longer".
# If str2 is longer than str1, print "str2 is longer".
# If both have equal length, print "Both are of equal length".


str1 = input("Enter First string: ")
str2 = input("Enter Second String: ")

# Check lengths of the strings
if len(str1) > len(str2):
    print(f"{str1} is the longest")
elif len(str2) > len(str1):
    print(f"{str2} is the longest")
else:
    print("Both are of equal length")


# 3.Given a list valid_ids = [101, 102, 103] and a variable user_id = 105, write a conditional statement that:
# Prints "Access Granted" if user_id is in valid_ids.
# Prints "Access Denied" if user_id is not in valid_ids.

user_id= (int(input("Enter ID: ")))
valid_ids= [101, 102, 103]

if user_id in valid_ids:
    print("Access Granted")
else:
    print("Access Denied")    



# 4.Given a variable value that could be of any type, write a conditional statement that:
# Prints "String Detected" if value is a string.
# Prints "Integer Detected" if value is an integer.
# Prints "Unknown Type" for any other type.

value= 345456

if type(value) == str :
    print("String Detected")
elif type(value) == int :
    print("Interger Detected")   
else:
    ("Unknown Type")      

# 5.Given x = 7 and y = 14, write nested conditional statements that print:
# "x and y are both even" if both x and y are even numbers.
# "Only y is even" if only y is even.
# "Neither x nor y are even" if both are odd.

x= 786
y= 14

if x%2==0:
    if y%2==0:
        print("x and y are both even")
    else:
        print("Only x is even")

else:
    if y%2==0:
        print("Only y is even")
    else:
        print("Neither x nor y are even")            
        

# The outer if checks if x is even.
# If x is even, it then checks if xyis even as well:
# If both are even, it prints "x and y are both even".
# If only x is even, it prints "Only x is even".
# If x is not even, the inner block checks if y is even:
# If only y is even, it prints "Only y is even".
# If neither is even, it prints "Neither x nor y are even".



