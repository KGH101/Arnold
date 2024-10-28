first_name = "Arnold"
second_name = "Ochieng"
age = "25"
print(type(age))

age=str(age)

print(type(age))

full_name = first_name + " " + second_name
print(full_name)

full_name = "Arnold Ochieng"
print(full_name[3])

full_name = "Arnold Ochieng"



full_name = "Arnold Ochieng"
f1 = full_name
f1 = full_name.upper()
print(f1)

f2 = f1.lower()
print(f2)
f3 = f2.capitalize()
print(f3)

f4 = full_name.find("o")
print(f4)


class_name = "   September Intake    "
cl= class_name.strip()
print(len(class_name))
print(len(cl))

last_name = "Arnold Ochieng"
last_name = last_name.replace("Arnold", "Fergie")
print(last_name)

name = "Arnold:Davies:Ochieng"
print(name.split(':'))

x = "Arnaaldchaaaaaaaaamp"
print(x.count("a"))

x = "Davaasaaayaa"
print(x.count("a"))

name = "Arnold:Davies:Ochieng"
print(name.split('/'))


