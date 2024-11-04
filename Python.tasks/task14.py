# Write a program that takes input of 2 values and adds them. The program should only accept numbers and floats only or otherwise d
# isplay an error “invalid character entered” and take the user to re-enter the inputs .
    
while True:
 try:
      input1=float(input("Enter the first number: "))
      input2=float(input("Enter the second number: "))
      result = input1 + input2
      print(result)
      break
 except:
     print("Invalid character entered")
   




