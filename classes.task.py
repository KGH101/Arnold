## 1.Create a class Animal with attributes species and sound.Add a method make_sound that prints: "The [species] goes [sound]!",Instantiate objects for different animals and call make_sound.

class Animals:
    def __init__(self,species, sound):
        self.species= species
        self.sound= sound
    def make_sound(self):
        return f"The {self.species} goes {self.sound}! "
    
dog= Animals("dog","woof")    
cow= Animals("cow","moos")
cat= Animals("cat","meows")

print(dog.make_sound())
print(cow.make_sound())
print(cat.make_sound())
        
        
## 2.Create a class Book with attributes like title, author, and year.
## Add a method that returns a description of the book.
## Create an object of Book and print out the description.

class Book:
    def __init__(self,title,author,year):
        self.title= title
        self.author= author
        self.year= year

    def describe(self):
        return f"{self.title} by {self.author} ,{self.year}" 
    
Book1= Book("The River and The Source","Margaret Ogolla",1994)
Book2= Book("Kidagaa Kimemuozea","Ken Walibora",2012)
print(Book1.describe())    
print(Book2.describe())    

## 3.Define a class BankAccount with attributes owner and balance (set balance to 0 by default).Add methods deposit and withdraw to modify the balance and a method get_balance to display the balance.
## Ensure that the withdraw method does not allow the balance to go negative.


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.balance+=amount   
            return f"{amount} deposited, your New Balance is {self.balance}"
        else:
            return "Invalid, Deposit amount cannot be less than zero"

    def withdraw(self,amount)  :
        if amount > self.balance:
            return f"insufficient balance to withdraw{amount}"
        
        else:
            self.balance-=amount
            return f"{amount} withdrawed and the new balance is {self.balance}"
        

    def get_balance(self):
        return f"Hello {self.owner} Current balance is {self.balance}"
    

person1= BankAccount("Arnold")
person1.deposit(1000)   
person1.withdraw(5000)
print(person1.get_balance())       

# Define a class Rectangle with attributes width and height.
# Add methods area and perimeter to calculate the area and perimeter of the rectangle.
# Instantiate a few rectangle objects and print their area and perimeter.

class Rectangle:
    def __init__(self, width, height):
        self.width= width
        self.height= height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) *2
    
rectangle1 = Rectangle(3, 11)
rectangle2 = Rectangle(4, 19)
rectangle3 = Rectangle(8, 14)


print(f"Area of Rectangle 1 is: {rectangle1.area()}, Perimeter is: {rectangle1.perimeter()}")
print(f"Area of Rectangle 2 is: {rectangle2.area()}, Perimeter is: {rectangle2.perimeter()}")
print(f"Area of Rectangle 3 is: {rectangle3.area()}, Perimeter is: {rectangle3.perimeter()}")
   
