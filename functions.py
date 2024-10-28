def hello():
    name = "Arnold"
    print(f"Hello, {name}")

hello()  

# create a function to calculate the area of a triangle
 

def area_triangle():
    base= 20
    height=10
    area = (base*height)* 0.5
    print(area)

area_triangle()   

# create a function that calculates the area a reactangle that takes users input

def area_rectangle():
    l = float(input("Enter Length:"))
    w = float(input("Enter width: "))
    area = (l*w)
    print(area)

area_rectangle()    


# checks if a number takes input from a user of a number and checks if a number is even number or odd number

def even_or_odd ():
    num = int(input("Enter Number:"))
    if num%2== 0:
        print(f"{num} Is even")
    else:
        print(f" {num} is Odd")    

even_or_odd()   

# 3 8 10 12 13