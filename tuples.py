# create tuple
# enclosed with ()
my_tuple=("josh","tony","arnold","stanley",1000,99)
print(my_tuple[3:])

# tuple = used to convert a data structure into a tuple
x =[1,2,3,4,5]
x= tuple(x)
print(type(x))

# convert tuple into a list
# list = used to convert data structure into a list
my_tuple=("josh","tony","arnold","stanley",1000,99)
my_tuple = list(my_tuple)
print(type(my_tuple))

y = ("a","b","c")
y= list(y)
y[2]="d"
y=tuple(y)
print(y)


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


a = ['a', 'b', 'c']
a[-1:]= ["d","e"]
print(a)

# x = [10, [3.141, 20, [30, 'baz', 2.718]], 'foo']
#x= [1][2][1:]

a = [1, 2, 7, 8]
a[2:2] = [3, 4, 5, 6]
print(a)

my_tuples=("age", 14,"location","kiambu",[100,300,500])
my_tuples= list(my_tuples)
my_tuples[4][1]= 600
print(my_tuples)

my_tuples= tuple(my_tuples)
print(my_tuples)