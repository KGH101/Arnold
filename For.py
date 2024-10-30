fruits=["banana","orange","pineapple","watermelon","apple"]

for fruit in fruits:
    if fruit =="ndizi":    
        print(fruit)


# range= used to create a list of numbers from a certain number

x=[1,2,3,4,5,6,7,8,9,10]
y=list(range(1,11))

num= list(range(1,1000))
print(num)

# iterate through number 20 t0 100

c= list(range(20,101))

for num in c:
    print(num)

for num in range(20,101):
    print(num)    

# iterate through numbers from 20 to 100 and only display even numbers    

numbers = list(range(20,101))
even_number= []
for i in numbers:
    if i%2==0:
        even_number.append(i)
print(even_number)        
       
# break, used to stop the loop

# Put in a list the first 10 odd numbers between 10 to 50.
numbers= list(range(20,51))
odd=[]
for i in numbers:
    if i%2!=0:
        odd.append(i)
    if len(odd)==10:
        break
print(odd)    
