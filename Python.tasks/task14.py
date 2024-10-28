# Write a program that takes input of 2 values and adds them. The program should only accept numbers and floats only or otherwise d
# isplay an error “invalid character entered” and take the user to re-enter the inputs .
while True:
    num1 = input("Enter num1: ")
    num2 = input ("Enter num2: ")

    if num1.isdigit() or  num2.isdigit() :
    
        num1 = int(num1)
        num2= int(num2)
        sum = num1 + num2
        break

    else:
        print("Invalid Character")    


print(sum)        