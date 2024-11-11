## Define a class Rectangle with attributes width and height.Add methods area and perimeter to calculate the area and perimeter of the rectangle.Instantiate a few rectangle objects and print their area and perimeter.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2


rect1 = Rectangle(4, 15)
rect2 = Rectangle(4, 13)
rect3 = Rectangle(8, 15)


print(f"Rectangle 1 - Area: {rect1.area()}, Perimeter: {rect1.perimeter()}")
print(f"Rectangle 2 - Area: {rect2.area()}, Perimeter: {rect2.perimeter()}")
print(f"Rectangle 3 - Area: {rect3.area()}, Perimeter: {rect3.perimeter()}")


## 2.Create a class Employee with attributes name and salary.Add a method give_raise that increases the salary by a given percentage.Instantiate an employee, give them a raise, and display their new salary.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def give_raise(self, percentage):
        self.salary += self.salary * (percentage / 100)
        return self.salary
# Instantiate an Employee object
employee = Employee("Arnold", 50000)

# Give the employee a 10% raise
employee.give_raise(10)

# Display the new salary
print(f"{employee.name}'s new salary is: {employee.salary}")

## 3.Create a base class Vehicle with attributes brand and model.
## Create two subclasses Car and Motorcycle that inherit from Vehicle and add unique methods to each subclass (e.g., honk for Car and rev_engine for Motorcycle).
## Instantiate both subclasses and call their methods.

# Base class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Car(Vehicle):
    def honk(self):
        return f"{self.brand} {self.model} goes 'Honk! Honk!'"


class Motorcycle(Vehicle):
    def rev_engine(self):
        return f"{self.brand} {self.model} goes 'Vroom! Vroom!'"


my_car = Car("Toyota", "Corolla")
my_motorcycle = Motorcycle("Yamaha", "MT-07")


print(my_car.honk())
print(my_motorcycle.rev_engine())
