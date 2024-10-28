# 3 8 10 12 13 using functions

# 3 Write a program which gets a phone number from a form input or terminal. Validates the phone number by checking if it starts with +254.. or 07.. or 7… or 254.. or 01... or  1.. Convert the number to start with +254… 
# e.g if a user enters “0712345678”, the program should display “+254712345678”
# e.g if a user enters “0112345678”, the program should display “+254112345678”
# e.g if a user enters “712345678”, the program should display “+254712345678”

def validate_num(phone_number):
 
   if phone_number [0:4]== "+254" and len(phone_number)==13:
      output= f"{phone_number} is valid"
   elif phone_number[0:2]== "07" and len(phone_number)==10:
      output= f"{phone_number} is valid"
   elif phone_number [0:1]=="7" and len(phone_number)==9:
      output=f"{phone_number} is vaild"
   elif phone_number [0:2]=="01" and len(phone_number)==10:
      phone_number = "+254" +phone_number[1:]
      output = f"{phone_number} is valid"
   elif phone_number [0:1]=="1" and len(phone_number)==9:
      phone_number = "+2541"+phone_number[1:1]
      output= f"{phone_number} is valid"
   else:
      output= "invalid number"

   return  output
 
phone_number = input("Enter Phone number:")
y= validate_num(phone_number)
print(y)
           

# 8 Write a program that takes as input the speed of a car e.g 80. If the speed is less than 70, it should print “Ok”. Otherwise, for every 5 km/s above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points.
#For example, if the speed is 80, it should print: “Points: 2”. If the driver gets more than 12 points, the function should print: “License suspended”.


def calculate_demerit_points(speed):
    speed_limit = 70
    demerit_points = (speed - speed_limit)/5
    max_demerit_points = 12

    if speed <= speed_limit:
        output  = ("OK")

    elif demerit_points > max_demerit_points :
        output = ("LICENCE SUSPENDED")

    else:
      output= (f"DEMERIT POINTS: {demerit_points}")


    return output
speed = int(input("Enter Speed:"))
s = calculate_demerit_points(speed)
print(s)


#10 Write a program that calculates the total stock in a company from the array/list below if we know that the stock is the last digit in every array/list.

prods = [['omo','30Kshs','300'], ['milk','50Kshs','200'],['bread','45Kshs','359'], ['coffee','5Kshs','79']]

def calc_stock(sum):
   sum_stock=0

   for prod in prods:
      stock= int(prod[-1])
      sum_stock+=stock
   return(f"Total stock is : {sum_stock}") 
y = calc_stock(sum)   
print(y) 


# 13 Write a program that takes the email and password as input from a user and checks if they are equal to “admin@mail.com” and password is “Admin@123” , if so then print  “Login is Successful” and if not print “Invalid username or password”. ONLY accept 3 tries after which it notifies you that you have been blocked.
  

def email_password_check():

    correct_password = "Admin@123"
    correct_email = "admin@gmail.com"
    attempts = 3

    for i in range(attempts):
       email = input("Enter Email: ")
       password= input("Enter Password: ")
       if email==correct_email and password==correct_password:
          output = "login is succesful"
          break
       else:
          remaining_tries= attempts-(i+1)
          if remaining_tries <=0:
             output = "you have been blocked"
          else :
             print(f"invalid email or password try again {remaining_tries} tries remaining")   

    return output          
    
result= email_password_check()
print(result)



       
         
         
   


   


# 12 Write a program that prints the largest of 4 inputs taken in from a user. Assume that the user would not enter any two numbers which are the same.

def largest_num(num1,num2,num3,num4):
   
   largest = max(num1,num2,num3,num4)

   if num1 > num2 and num1 > 3 and num1 > num4:
      value= (f"{num1} is the largest")
   elif num2 > num1 and num2 > 3 and num2 > num4:
     value= (f"{num2} is the largest")
   elif num3 > num1 and num3 > num2 and num3 > num4:
      value= (f"{num3} is the largest")
   elif num4 > num1 and num4 > 2 and num4 > num3: 
     value= (f"{num4} is the largest")
   else:
      value ("ERROR, DO NOT REPEAT A NUMBER")

   return  value
num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))
num3 = float(input("Enter num3: "))
num4 = float(input("Enter num4: "))     

x= largest_num(num1,num2,num3,num4)
print(x)





    