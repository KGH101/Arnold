# Write a program that takes the date of birth of a person and the program outputs the age in terms of years,months,days TODAY.
from datetime import datetime
today = datetime.now()

dob = input("Enter your dob (date/month/year): ")

t_dob =dob.split("/")

if len(t_dob) > 3 or int(t_dob[0])> 31 or int(t_dob[1]) > 12 :

    print("Wrong Date Format")

else:
    y = today.year - int(t_dob[2])
    m = today.month-int(t_dob[1])
    d = today.day - int(t_dob[0])

    if d < 0:
        m= m-1
        d = d+31

    if m < 0:
        y=y-1
        m=m+12

print(f"You are {y} years {m} months {d} days old")




