#Convert a float to an integer with an inbuilt function in Python
temp = 56.8926
temp = round(temp)
print(temp)

#Convert the float below to give the results as follows
#temp = 56.8926 to 56.89
temp = 56.8926
rounded_num = round(temp,2)
print(rounded_num)

#Convert the float below to give the results as follows
#temp = 56.8926 to 56.893
temp = 56.8926
rounded_temp= round(temp,3)
print(rounded_temp)

#Convert the float below to give the results as follows
#temp=56.8926 to 8.926

temp = 56.8926
num= str(temp)
print(num)

num = "56.8926"
num1 = (num.replace(".",""))
print(num1)

num1= "568926"
num2= (num1[2:6])
print(num2)
