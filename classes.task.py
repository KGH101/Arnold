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

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance for this withdrawal.")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return f"Current balance is {self.balance}"


account = BankAccount("Alice")

# Depositing money
account.deposit(100)

# Withdrawing money
account.withdraw(50)

# Attempt to withdraw more than the balance
account.withdraw(100)

# Display the balance
print(account.get_balance())
