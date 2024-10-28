# If statement
# else otherwise
a= 5
b= 10

if a>b:
    print("a is greater")
else:
    print("b is greater")    

# take the users input of a number   input ()
# check if the number is even
# if the number is not even display odd number

number= (input("enter number"))
number = int(number)

if number%2==0:
    print("even number")
else:
    print("odd number")   


 # take the users input of a number   input ()
# check if the number is odd
# if the number is not even display odd number


number= input("enter number:")
number= int(number)

if number%2!=0:
    print("odd number")
else:
    print("even number")   

# take the users input of a number   input ()
# check if the number is odd
# if the number is not even display odd number

number= input("enter number:")
number= int(number)


if number%2!=0  and  number>30:
    print("odd number")
else:
    print("even number") 


# grading system
# > 80 A
# >70  <80 B
# > 60 C
# else> D
# if elif else

marks= int(input("Enter Marks"))
if marks>=80:
    print("grade A")
elif marks>=70 and marks<80:
    print("grade B")
elif marks>60 and marks<70:
    print("grade C")
else:
    print("Grade D")    

# take users input of 3 numbers
# Find the largest number on the 3 inputs
# assume the user wont enter 2 similar numbers


# Taking input from the user
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

if num1 > num2 and num1 > num3:
    print(f"{num1}  is the largest")
elif num2 > num1 and num2 > num3:
    print(f"{num2} is the largest")
else:
    print(f"{num3}is the largest")

    # formatted strings is used to insert variables insude a strin


# nested if
# users input of marks
# check if the marks are between 0 and 100
# # > 80 A
# >70  <80 B
# > 60 C
# else> D
# else invalid
marks= int(input("enter marks"))

if marks>=0 and marks <=100:

 if marks>80:
    print("grade A")
 elif marks>70 and marks<80:
    print("grade B")
 elif marks>60 and marks<70:
    print("grade C")
 else:
    print("Grade D")  
else:
    print("invalid marks")



