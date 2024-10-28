# 1

first_name= "Arnold"
last_name= "Davies"

full_name= first_name+ " "+ last_name
print(full_name)

# 2 

word="PYTHON"
first_char = word[0]     
last_char = word[-1]      
print(f"First character: {first_char}")
print(f"Last character: {last_char}")


# 3

phrase= "Learning Python is fun!"
sliced_word = phrase[9:15]
print(sliced_word)

# 4

text = "reverse this"
reversed_text = text[::-1] # text[::-1] slices the string from the end to the start, effectively reversing it.
print(reversed_text)

# 5 replace world with python

greeting= "Hello World"
greeting= greeting.replace("World", "Python")
print(greeting)

# 6 uppercase to lowercase

msg= "Python Programming"

msg_upper= msg.upper
msg_lower= msg.lower

print(msg_upper())
print(msg_lower())

# 7 count occurrences "s"

sentence= "This is a simple sentence"
x= (sentence.count("s"))
print(x)

# 8 check substring presence "future"

qoute= "The best way to predict the future is to create it"

substring = "future"

print (qoute.count("future"))

if substring in qoute: # The in keyword checks if the substring "future" exists within the given text.
    print(f'The substring "{substring}" is present.')
else:
    print(f'The substring "{substring}" is not present.')




# 9 string length

description= "Data Science"
length= (len(description))
print(length)

# 10 remove whitespace

name= "   John Doe  "
name1= name.strip()
print(name1)






