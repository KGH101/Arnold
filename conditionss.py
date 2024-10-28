if 20> 40:
    print(f"{20} is greater")
else:
    print(f"{20} is lesser")


# delare a variable marks then check if the marks is above 50 and less than 100 print pass, otherwise, print fail

marks=(int(input("Enter Number: ")))


if marks>= 50 and marks<=100 :
    print("Pass")
else:
    print("fail")    


 # declare a variable number, check if the number is even , otherwise print odd


number= (int(input("Enter number: ")))

if number%2==0:
    print(f" {number} is even number")
else:
    print (f" {number} is odd number")   

# grading

marks= (int(input("Enter Marks: ")))

if marks >=90 and marks<=100:
    print("A")
elif marks >=80 and marks<90:
    print("B") 
elif marks >=70 and marks<80:
    print("C")
elif marks >=60 and marks<70:
    print("D")
elif marks >=50 and marks<60:
    print("E")
else:
    print("Fail")   


# write a program that takes age from the user
# if age is 60 or above or above print older
# if age is 18 and above print adult
# otherwise print minor                 

age= (int(input("Enter Age: ")))

if age >=60:
    print("Older")
elif age >=18 and age<60:
    print("Adult")
else:
    print("Minor")   


# nested if statements
# give 100 discount on purchase above 1000
# give 200 discount on purchase above 5000
# less than 1000, no discount         

purchase= (int(input("Enter Purchase: ")))

if purchase>1000:
    print("100 discount")
    if purchase>5000:
        print("200 discount")
else:
    ("No Discount")   


# write a program that takes users age as input
# if age is 18 and above, check if the have a drivers licence, if they do,print "eligible to drive"
# if they dont have a drivers licence, print "you are not eligible to drive"
# otherwise, print "you are not eligible to drive"
         
age= (int(input("Enter Age: ")))

if age >=18:

    licence= input("Do you have a licence yes/no: ").strip().lower()
    if licence=="yes":
        print("You are eligible to drive")
    else:
        print("You are not eligible to drive")  

else:
    print("You are too young to drive")   

# write a program that
# takes users credit score and annual income as input
# if the credit score is above 700, check if the income is above $50000
# if both conditions are met, print "loan approved"
# if only the credit score is high, print "Income requirement not met"
# if credit score is below 7oo, print "Credit score too low"
           

credit_score= (int(input("Enter your credit score: ")))
annual_income= (int(input("Enter your annual income")))

if credit_score >700:

    if annual_income > 50000:
        print("loan approved")

    else:
        print("Income requirement not met")  

else:
    print("Credit score too low")          