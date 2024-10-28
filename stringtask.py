class_name = "  JOHn "
cn = class_name.strip()
print(len(class_name))
print(len(cn))

class_name = "JOHn"
N1 = class_name
N1 = class_name.lower()
print(N1)




sentence_one = "The Dog Breed is German Shepherd"
sliced_one = (sentence_one[8:23])
print(sliced_one)

sentence_two = "Defeats for the Clinton forces, this was a moment of triumph"
sliced_two = (sentence_two[16:30])
print(sliced_two)


name = "The lazy dog; ran so fast; it hit the wall"
print(name.split(';'))
print(len(name))


first_name = " Joh.n"
last_name = " Do,e"
print(first_name.replace('.',''))


last_name = " Do,e"
print(last_name.replace(',','')) 

first_name = " Joh.n"
last_name = " Do,e"
print(first_name.replace('.','') + last_name.replace(',',''))



r = '["E","W","C"]'
r=r.replace('[','').replace(',','').replace('"','').replace(']','')
print(r)