# Write a python program that takes from a user 5 inputs (maths, eng, swa,
# sci, sos).
# Create a function that calculates the total marks another the average
# marks ,then a functions that finds the grade according to the table below.
#Use the value from total to get the average and average to find the grade.
#A > 79 , B - 60 to 79, C - 59 to 49, D - 40 to 49, E - less 40


def calculate_total(a, b, c, d, e):
    total_marks= (a+b+c+d+e)
    return total_marks



maths = float(input("Enter marks for Maths: "))
eng = float(input("Enter marks for English: "))
swa = float(input("Enter marks for Swahili: "))
sci = float(input("Enter marks for Science: "))
sos = float(input("Enter marks for Social Studies: "))  


total_marks= calculate_total(maths,eng,swa,sci,sos)
print(f"The totak marks is: {total_marks}")


   
def get_average(total_marks) :
    average = total_marks/5
    return average

avg= get_average(total_marks)
print(f"The average is: {avg}")


def get_grade(average):
     
    if average> 79:
        return 'A'
    elif average >= 60:
        return 'B'
    elif average>= 50:
        return 'C'
    elif average>= 40:
         return 'D'
    else:
        return 'E'
     
grade = get_grade(avg)
print(f"The grade is: {grade}")
   

