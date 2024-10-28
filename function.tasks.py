# 8 Write a program that takes as input the speed of a car e.g 80. If the speed is less than 70, it should print “Ok”. Otherwise, for every 5 km/s above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points.
#For example, if the speed is 80, it should print: “Points: 2”. If the driver gets more than 12 points, the function should print: “License suspended”.


def calculate_demerit_points():
   speed = int(input("Enter Speed: "))
   speed_limit = 70
   demerit_points = (speed - speed_limit)/5
   max_demerit_points = 12

   if speed <= speed_limit:
      print("OK")

   elif demerit_points > max_demerit_points :
      print("LICENCE SUSPENDED")

   else:
      print(f"DEMERIT POINTS: {demerit_points}")


calculate_demerit_points()  



#10 Write a program that calculates the total stock in a company from the array/list below if we know that the stock is the last digit in every array/list.

prods = [['omo','30Kshs','300'], ['milk','50Kshs','200'],['bread','45Kshs','359'], ['coffee','5Kshs','79']]

def calc_stock():
   total_stock=0

   for prod in prods:
      stock= int(prod[-1])
      total_stock+=stock
   print(f"Total stock is {total_stock}")   
calc_stock()   




# 12 Write a program that prints the largest of 4 inputs taken in from a user. Assume that the user would not enter any two numbers which are the same.


def largest_num():
   
   num1 = float(input("Enter num1: "))
   num2 = float(input("Enter num2: "))
   num3 = float(input("Enter num3: "))
   num4 = float(input("Enter num4: "))

   if num1 > num2 and num1 > 3 and num1 > num4:
      print(f"{num1} is the largest")
   elif num2 > num1 and num2 > 3 and num2 > num4:
     print(f"{num2} is the largest")
   elif num3 > num1 and num3 > num2 and num3 > num4:
      print(f"{num3} is the largest")
   elif num4 > num1 and num4 > 2 and num4 > num3: 
     print(f"{num4} is the largest")
   else:
      print("ERROR, DO NOT REPEAT A NUMBER")


largest_num()      
  


       
        
# 13 Write a program that takes the email and password as input from a user and checks if they are equal to “admin@mail.com” and password is “Admin@123” , if so then print  “Login is Successful” and if not print “Invalid username or password”. ONLY accept 3 tries after which it notifies you that you have been blocked.
  
def email_password_check():

    email = input("Enter Username :")
    password = input("Enter password: ")
    correct_password = "Admin@123"
    correct_email = "admin@gmail.com"
    max_attempts = 3


    if email == correct_email and  password == correct_password:
        print("Login is Succesfull")

    elif max_attempts >3:
        print("ACCOUNT BLOCKED")

    else:
        print(f"Incorrect Username or Password, you have {max_attempts-1} attempts left")  
   

email_password_check()              


# 3 Write a program which gets a phone number from a form input or terminal. Validates the phone number by checking if it starts with +254.. or 07.. or 7… or 254.. or 01... or  1.. Convert the number to start with +254… 
# e.g if a user enters “0712345678”, the program should display “+254712345678”
# e.g if a user enters “0112345678”, the program should display “+254112345678”
# e.g if a user enters “712345678”, the program should display “+254712345678”



def validate_num():
 
   phone_number = input("Enter Phone number:")

   if phone_number [0:4]== "+254" and len(phone_number)==13:
      valid= f"{phone_number} is valid"
   elif phone_number[0:2]== "07" and len(phone_number)==10:
      valid= f"{phone_number} is valid"
   elif phone_number [0:1]=="7" and len(phone_number)==9:
      valid =f"{phone_number} is vaild"
   elif phone_number [0:2]=="01" and len(phone_number)==10:
      phone_number = "+254" +phone_number[1:]
      valid = f"{phone_number} is valid"
   elif phone_number [0:1]=="1" and len(phone_number)==9:
      phone_number = "+2541"+phone_number[1:1]
      valid = f"{phone_number} is valid"
   else:
      valid = "invalid number"
   print(valid)      


validate_num()                     






    