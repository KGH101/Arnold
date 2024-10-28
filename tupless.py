# create tuple
# enclosed with ()

marks=(100,300,250,160,450,600)
print(type(marks))
marks= list(marks)
print(type(marks))

marks= tuple(marks)
print(type(marks))


days = ("monday","tuesday","wednesday","thursday",
"friday","saturday","sunday")

#1. Find wednesday using an index
d = days[2]
print(d)

#2. Using a function a find the length of the tuple.

d= len(days)
print(d)

#3. Replace Thursday with Thur
days = ("monday","tuesday","wednesday","thursday",
"friday","saturday","sunday")
days= list(days)
days[3]="thur"
days=tuple(days)
print(days)


