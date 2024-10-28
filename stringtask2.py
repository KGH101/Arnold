#Clean up the following variable to give the clean version in lower case. Using inbuilt methods in the str class
#name = “ JOHn .“ to “john”

name= "JOHn"
n= name.lower()
n= name.upper()
print(n)

#Slice the below string to get you the resulting sentence:
# sentence_one = “The Dog Breed is German Shepherd” only display “Breed is German”
# sentence_two = “Defeats for the Clinton forces, this was her moment of triumph” only display “Clinton
#forces”

sentence_one = "The Dog Breed is German Shepherd"
sliced_one = (sentence_one[8:23])
print(sliced_one)

sentence_two = "Defeats for the Clinton forces, this was her moment of triumph"
sliced_two = (sentence_two[16:30])
print(sliced_two)

#Split the below sentence using a semicolon i.e ; And display length of the result.
#“The lazy dog; ran so fast; it hit the wall.”
name = "The lazy dog; ran so fast; it hit the wall"
print(name.split(";"))

#first_name=" Joh.n" last_name= Clean up and display Full name i.e John Doe

first_name = " Joh.n"
n = (first_name.replace(".",""))
print(n)

last_name = " Do,e"
l = (last_name.replace(",",""))
print(l)

#Having the string r ='["E","W","C"]' #Manipulate it to display EWC
r = '["E","W","C"]'
r = r.replace('[','').replace(',','').replace('"','').replace(']','')
print(r)
