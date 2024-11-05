# block of code that perfoms a specific task and can only run when they are called
# takes in some data, 
# perfoms some operation on the data and returns an output
# define a fuction, give it a name, def name ():


# create a function to calculate the area of a triangle
 

def area_triangle():
    base= 20
    height=10
    area = (base*height)* 0.5
    print(area)

area_triangle()   

# create a function that calculates the area a reactangle that takes users input
# Parametres = variables used inside a function

def area_rectangle():
    l = float(input("Enter Length:"))
    w = float(input("Enter width: "))
    area = (l*w)
    print(area)

area_rectangle()  

# Area of a triangle using parametetrs and arguments


def area_triangle(base,height):
    area_tri=(base*height)*0.5
    return area_tri
x=area_triangle(20,50)
print(x)

# checks if a number takes input from a user of a number and checks if a number is even number or odd number

def check_even_odd(num):
    if num % 2 == 0:
        result= "Even"
    else:
        result="Odd"
    return  result  
number = int(input("Enter Number:"))
y=check_even_odd(number)
print(y)

# 12 Write a program that prints the largest of 4 inputs taken in from a user. Assume that the user would not enter any two numbers which are the same.


def largest_num(num1,num2,num3,num4):
   
   if num1 > num2 and num1 > 3 and num1 > num4:
      result= f"{num1} is the largest"
   elif num2 > num1 and num2 > 3 and num2 > num4:
     result= f"{num2} is the largest"
   elif num3 > num1 and num3 > num2 and num3 > num4:
      result= f"{num3} is the largest"
   else: 
     result= f"{num4} is the largest"

   return result

number1 = float(input("Enter num1: "))
number2 = float(input("Enter num2: "))
number3 = float(input("Enter num3: "))
number4 = float(input("Enter num4: "))

value= largest_num(number1,number2,number3,number4)
print(value)

