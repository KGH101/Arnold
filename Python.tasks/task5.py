# Implement a program that takes 3 form inputs or from the terminal, and stores them in three variables. Return the largest of the three. Do this without using the the inbuilt max () function!


Num1 = int(input("Enter First Number: "))
Num2 = int(input("Enter Second Number: "))
Num3 = int(input("Enter Third Number: "))

if Num1 > Num2 and Num1 > Num2:
    print("Num1 is the largest")
elif Num2 > Num1 and Num2 > Num3:
    print("Num2 is the largest")
else:
    print("Num3 is the largest")        