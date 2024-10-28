days = {"monday","tuesday","wednesday","thursday",
"friday","saturday","sunday","sunday","sunday","sunday"}
print(days)

# Remove friday and sunday from the set using methods.
#Add them back to the setTask
days = {"monday","tuesday","wednesday","thursday",
"friday","saturday","sunday","sunday","sunday","sunday"}
print(days)
days= list(days)
days.remove("friday")
days.remove("sunday")
days = set(days)
print(days)

