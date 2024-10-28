def hello(name):
    
    print(f"Hello, {name}!")

hello("Arnold") 



def hello(name):
    return(f"Hello, {name}!")

full_name= input("Enter your name:")    
x= hello(full_name)
print(x)


# create a function to calculate the area of a triangle
 
def triangle_area(a,b):
    area = (a*b)*0.5
    return area

base= int(input("base:"))
height = int(input("Height:"))
x = area = triangle_area(base,height)
print(x)
   
    
 # create a function that calculates the area a reactangle that takes users input

def rectangle_area (a,b):
    area = (a*b)
    return area
length = int(input("Length:"))
width= int(input("Width:"))
x = area= rectangle_area(length,width)
print(f"The are is: {x}")
   

# checks if a number takes input from a user of a number and checks if a number is even number or odd number

def odd_or_even (n):
    if n%2== 0:
        value=(f"{n} Is even")
    else:
        value=(f" {n} is Odd")    
    return value
number= int(input("Number:"))
x= odd_or_even(number)
print(x)


# 3 8 10 12 13 using functions


