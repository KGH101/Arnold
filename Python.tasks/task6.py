# Write a program that lets the user input a password. Give them only 4 attempts to check the passwords entered against “admin@123”. If the password is correct access is granted. After you show them a message , the account is blocked.

correct_password = "admin@123"
attempts = 4

for i in range(attempts):
    password = input("Enter password: ")
    remaining_attempts = attempts - (i + 1)
    
    if password == correct_password:
        result="Access granted."
        break
    elif remaining_attempts > 0:
        print(f"Incorrect password. You have {remaining_attempts} attempts left.")
        
    else:
        result="Account blocked."

print(result)    

correct_password = "admin@123"
attempts = 4

# OR

for i in range(attempts):
    password = input("Enter password: ")
    remaining_attempts = attempts - (i + 1)
    
    if password == correct_password:
        result="Access granted."
        break

    else:
        print(f"Incorrect password. You have {remaining_attempts} attempts left.")

        if remaining_attempts==0:
            result="Account Blocked"


print(result)    

# OR

correct_password = "admin@123"
max_attempts = 4
attempts = 0

while attempts< max_attempts:
    password = input("Enter Password: ")
    if password == correct_password:
        result="Acces granted"
        break
    else:
        attempts+1
        print(f"Incorrect password. You have {remaining_attempts} attempts left.")

if attempts == max_attempts:
    result="Account Blocked"

print(result)    