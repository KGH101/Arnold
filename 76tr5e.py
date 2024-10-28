#10 Write a program that calculates the total stock in a company from the array/list below if we know that the stock is the last digit in every array/list.

prods = [['omo','30Kshs','300'], ['milk','50Kshs','200'],['bread','45Kshs','359'], ['coffee','5Kshs','79']]

def calc_stock():
   total_stock=0

   for prod in prods:
      stock= int(prod[-1])
      total_stock+=stock
   print(f"Total stock is {total_stock}")   
calc_stock()   




maths = float(input("Enter marks for Maths: "))
        eng = float(input("Enter marks for English: "))
        swa = float(input("Enter marks for Swahili: "))
        sci = float(input("Enter marks for Science: "))
        sos = float(input("Enter marks for Social Studies: "))


        total = calculate_total(maths, eng, swa, sci, sos)
        average = calculate_average(total)

        
        grade = determine_grade(average)

    
        print(f"Total Marks: {total}")
        print(f"Average Marks: {average:.2f}")
        print(f"Grade: {grade}")



return maths + eng + swa + sci + sos

def calculate_average(total):

    return total / 5

def get_grade(average):
    
    if average > 79:
        return 'A'
    elif average >= 60:
        return 'B'
    elif average >= 50:
        return 'C'
    elif average >= 40:
        return 'D'
    else:
        return 'E'