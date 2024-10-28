# Prompt the user for a number either on a form input or the terminal. Depending on whether the number is even or odd, display  either “odd” or “even” to the user.

number = int(input("Enter Number: "))

if number % 2 ==0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")    