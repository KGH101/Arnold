#Write that prompts the user to input student marks. The input should be between 0 and 100.Then output the correct grade: 
# A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40

student_mark = int(input("Enter Student Marks: "))

if student_mark <=100 and student_mark >79:
    print("A")
elif student_mark <=79 and student_mark > 60:
    print("B")
elif student_mark <=59 and student_mark >  49: 
    print("C")   
elif student_mark <=49 and student_mark > 40:
    print("D")  
elif student_mark < 40:
    print("E")
else:
    print ("Enter Valid Marks")   




# or int(t_dob[2]) < 1900 or int (t_dob[2]) > 2023 :
