# Write a program that lets the user input a password. Give them only 4 attempts to check the passwords entered against “admin@123”. If the password is correct access is granted. After you show them a message , the account is blocked.

correct_password = "admin@123"

max_attempts = 4

# loop to give user 4 attempts
for i in range(max_attempts):

    password = input("Enter password: ")
    
    if password == correct_password:
        print("Access granted.")
        # i is the current attempt
    elif i == max_attempts - 1:
        print("Account is blocked")
    else:
        print(f"Incorrect Password, you have {max_attempts - i- 1} attempts left")    
