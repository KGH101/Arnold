# Defined exactly same way as a list except you use round brackets i.e

days = ("monday","tuesday","wednesday","thursday",
"friday","saturday","sunday")

#1. Find wednesday using an index

d = days[2]
print(d)
#2. Using a function a find the length of the tuple.
days = ("monday","tuesday","wednesday","thursday",
"friday","saturday","sunday")

l = len(days)
print(l)
#3. Replace Thursday with Thur
days = list(days)
print(days)
days[3]="Thur"
days = tuple(days)
print(days)