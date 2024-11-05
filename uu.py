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
  
