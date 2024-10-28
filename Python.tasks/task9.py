# Write a program called stars. It should prompt the user for a number, and it should print the number of stars till the number entered.
# Example If rows is 5, it should print the following:
# *
# **
# ***
# ****
# *****.....

num = int(input("Enter a number: "))

count=0
for i in range(1,num+1):
    value=("*"*i)
    count=count+1
    if count==num:
        value=value+("."*i)
    print(value)
