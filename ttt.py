
# Take three inputs from a user, separately. Print the largest of the numbers.

num1 = int(input("Enter First Number:"))
num2 = int(input("Enter Second Number:"))
num3 = int(input("Enter Third Number:"))

if num1>num2 and num1>num3:
    print(f"{num1} is the largest")
elif num2>num1 and num2>num3:
    print(f"{num2} is the largest")
else:
    print(f"{num3} is the largest")              

# Determine what type of data is taken in as input.
# Take as input from a user the temperature if the temperature is above 30°C display “The temperature is too
# high”,if the temperature is above 15 display “Normal temperature” otherwise display “Cold temperature”

temperature = int(input("Enter the Temperature:"))

if temperature>30:
    print("The temperature is too high")
elif temperature>15:
    print("Normal Temperature")
else:
    print("Cold Temperature")        
# Write a Python program that checks if a variable x is between 10 and 20 (inclusive)
# and if another variable y is greater than 100. If both conditions are true, print "Conditions met", otherwise print
#"Conditions not met"

x = int(input("Enter Number:"))
y= int(input("Enter Number:"))

if x>10 and x<20:
    print("Conditions met")
elif y>100:
    print("Conditions met")
else:
    print("Conditions not met")        
# Write a Python program that checks if a variable password is equal to the string "secret123". If it is, print "Access
# granted", otherwise print "Access denied"

password = input("Enter Password:")

if password=="secret123":
    print("Access granted")
else:
    print("Access denied")    
# Write a Python program that checks if a variable student_score is greater than 90. If true, check if the attendance is
#greater than 80. If both conditions are true, print "Excellent student", otherwise print "Good score, but attendance
#needs improvement"

student_score = int(input("Enter Score:"))
attendance = int(input("Enter Attendance:"))

if student_score>90 and attendance>80:
    print("Excellent Student")
else:
    print("Good score, but attendance needs improvement")    
    