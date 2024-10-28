
# Take three inputs from a user, separately. Print the largest of the numbers.
Num1 = int(input("Enter number 1:"))
Num2 = int(input("Enter number 2:"))
Num3 = int(input("Enter number 3:"))

if Num1 > Num2 and Num1> Num3:
    largest=Num1
elif Num2 > Num1 and Num2> Num3:
    largest=Num2
else:
    largest=Num3      

print(f"{largest} is the largest")
# Hint: Determine what type of data is taken in as input.

# Take as input from a user the temperature if the temperature is above 30°C display “The temperature is too
# high”,if the temperature is above 15 display “Normal temperature” otherwise display “Cold temperature”

temperature = int(input("Enter the temperature:"))

if temperature > 30:
    print("The temperature is too high")
elif temperature > 15:
    print("Normal temperature")
else:
    print("Cold temperature")




# Write a Python program that checks if a variable x is between 10 and 20 (inclusive)
# and if another variable y is greater than 100. If both conditions are true, print "Conditions met", otherwise print
#"Conditions not met"


x = int(input("Enter Number:"))
y = int(input("Enter Number:"))



if x >= 10 and x <= 20 and y > 100:
    print("Conditions met")
else:
    print("Conditions not met")


# Write a Python program that checks if a variable password is equal to the string "secret123". If it is, print "Access
# granted", otherwise print "Access denied"
password = input("Enter Password:")
correct_password= "secret123"

if password == correct_password:
    print("Access granted")
else:
    print("Access denied")



# Write a Python program that checks if a variable student_score is greater than 90. If true, check if the attendance is
# greater than 80. If both conditions are true, print "Excellent student", otherwise print "Good score, but attendance
# needs improvement"


student_score = float(input("Enter Student Score: "))
attendance = int(input("Enter The Attendance: "))

if student_score >90:
   if attendance >80:
        print("Excellent Student")
   else:
       print("Good score, but attendance needs improvement")    

else:
    print("poor score")
        
    

   

# write a python program that checks if a variable num is positive. if it is, further checck if it is divisible byth both two and 3

num= int(input("Enter Number:"))

if num>=0:
    if num%2==0  and num%3==0:
        print(f"{num} positive and divisible by 2 and 3")
    else:
        print(f"{num} positive number but not divisible by 2 or 3")   
else:
    print("negative number")        




# writa a python program that checks a username and password, if both are correct, print login successful, if either the username or paasord is incorrect, print login failed

username= input("Enter Username:")
password = input("Enter Password:")
correct_password = "ARNOLD1234"
correct_username= "daviesarnol99@gmail.com"
if correct_password=="ARNOLD1234" and correct_username=="daviesarnold@gmail.com":
    print("Login successful")
else:
    print("Login failed")    


    # Write a python program that checks if a given string is a palindrome (reads the same forward and backward)

word = input("Enter a Word:")
if word==word[::-1]:
    print("The word is a palindrome")
else:
    print("the word is not a palindrome")    



# Write a python program that calculates the body mass index and categorises it into underweight, normal weight, overweight, and obesity based pon standard BMI ranges


# Write a python program that prints the numbers from 1 to 100. for multiples of three, print "fizz" instead of the number, and for the multiples of five, print "Buzz". For numbers which are multiple of both three and five, print "FizzBuzz"