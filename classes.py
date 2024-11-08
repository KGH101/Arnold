# define class named car

class Car:
    # constructor method
    def __init__(self,color,brand,shape):
        self.color=color
        self.brand=brand
        self.shape=shape

    def describe(self):
        return f"the color of this car is {self.color} and the brand is {self.brand} the shape is {self.shape}"

mycar=Car("red","BMW","wagon")
car1=Car("green","Audi","sedan")


print(mycar.color)
print(car1.brand)
print(mycar.describe())
print(car1.describe())

# 1 create a class called student with attributes name and age
# create an object of student and call the introduce method
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hello, my name is: {self.name}, and Iam {self.age} years old"

student1 = Student("Arnold", 20)
student2= Student ("Fergie", 30)
print(student1.introduce())
print(student2.introduce())

# Define a class Calculator with methods add, substract,multiply and divide that perfom the respective operations on two numbers
# create an object of Calculator and use it to perfom some calculations

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b


calc = Calculator(100, 5)

print(f"Addition: {calc.add()}" )
print(f"Subtraction: {calc.subtract()}" )
print(f"Multiply: {calc.multiply()}" )
print(f"Divide: {calc.divide()}" )



        