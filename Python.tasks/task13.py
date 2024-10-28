# Write a program that takes the email and password as input from a user and checks if they are equal to “admin@mail.com” and password is “Admin@123” , if so then print  “Login is Successful” and if not print “Invalid username or password”. ONLY accept 3 tries after which it notifies you that you have been blocked.

correct_password = "Admin@123"
correct_email = "admin@gmail.com"

max_attempts = 3


# loop to give it 3 attempts
for i in range(max_attempts):

    email = input("Enter Username :")
    password = input("Enter password: ")

    if email == correct_email and  password == correct_password:
        print("Login Succesfull")

    elif i == max_attempts - 1:
        print("ACCOUNT BLOCKED")

    else:
        print(f"Incorrect Username or Password, you have {max_attempts-i-1} attempts left")        





        import datetime
today = datetime.datetime.now()
dob = input("enter you dob (year/month/day): ")
print(dob)

dob_split = dob.split("/")
dob_year = int(dob_split[0])
dob_month = int(dob_split[1])
dob_day = int(dob_split[2])

years = today.year-dob_year
months = today.month - dob_month
days = today.day-dob_day


if days < 0:
    months -= 1
    # Get the number of days in the last month
    last_month = today.month - 1 if today.month > 1 else 12
    last_month_year = today.year if last_month != 12 else today.year - 1
    days += (datetime.datetime(last_month_year, last_month, 1) - datetime.timedelta(days=1)).day

if months < 0:
    years -= 1
    months += 12

print(f'{years} years {months} months {days} days')


    


    
    


    
  
    




     

