## Write a program that takes input of someone's basic salary and benefits, adds them to find the gross salary then uses  the gross salary to find the NHIF. 
## To find the Kenya NHIF Rate using THIS LINK:  

## fuction to calculate gross salary


def calc_gross_salary(basic_salary, benefits):

    gross_salary= basic_salary + benefits
    return gross_salary


basic_salary = float(input("Enter Basic Salary: "))
benefits = float(input("Enter Benefits: "))
gross_salary= calc_gross_salary(basic_salary,benefits)
print(f"The gross salary is: {gross_salary}")

# Use the gross salary to find the NHIF

def get_nhif(gross_salary):

    nhifContribution=0

    if gross_salary <= 5999:
        nhifContribution = 150
    elif gross_salary <= 7999:
        nhifContribution = 300
    elif gross_salary <= 11999:
        nhifContribution = 400
    elif gross_salary<= 14999:
        nhifContribution = 500
    elif gross_salary <= 19999:
        nhifContribution = 600
    elif gross_salary <= 24999:
        nhifContribution = 750
    elif gross_salary <= 29999:
        nhifContribution = 850
    elif gross_salary <= 34999:
        nhifContribution = 900
    elif gross_salary <= 39999:
        nhifContribution = 950
    elif gross_salary <= 44999:
        nhifContribution = 1000
    elif gross_salary <= 49999:
        nhifContribution = 1100
    elif gross_salary <= 59999:
        nhifContribution = 1200
    elif gross_salary <= 69999:
        nhifContribution = 1300
    elif gross_salary <= 79999:
        nhifContribution = 1400
    elif gross_salary <= 89999:
        nhifContribution = 1500
    elif gross_salary <= 99999:
        nhifContribution = 1600
    else:
        nhifContribution = 1700
    
    return nhifContribution

nhif = get_nhif(gross_salary)
print(f"NHIF CONTRIBUTION: {nhif}" )

## Continue with the program above, then use  the gross salary to find the NSSF. 
##  To find the Kenya NSSF Rate  using 6% of the Gross Salary. BUT ONLY A MINIMUM OF 18,000 Gross Salary CAN BE USED IN NSSF. 


def get_nssf(a):

    nssf_contribution=0

    if a>=0 and a<=18000:
        nssf_contribution= a*0.06
    else:
        nssf_contribution=18000*0.06
    
    return nssf_contribution

nssf= get_nssf(gross_salary)
print(f"NSSF CONTRIBUTION: {nssf}")


## Continue with the same program and calculate an individual’s NHDF using:
## i.e NHDF = gross_salary *  0.015

def get_nhdf(a):
    nhdf_contribution = a * 0.015

    return nhdf_contribution

nhdf= get_nhdf(gross_salary)
print(f"NHDF: {nhdf}")



## Calculate the taxable income.
## i.e taxable_income = gross salary - (NSSF + NHDF + NHIF) 

def get_taxable_income(gross_salary, nssf, nhdf, nhif):
    taxable_income = gross_salary - (nssf+nhdf+nhif)

    return taxable_income

taxable_income = get_taxable_income(gross_salary, nssf, nhif, nhdf)
print(f"Taxable Income: {taxable_income}")



## Continue with the same program and find the person's PAYEE using the taxable income above.
## Find the Kenya PAYEE Tax Rate using THIS LINK
## Less Relief 

## First Ksh 24,000: Taxed at 10%
## Next Ksh 8,333: Taxed at 25%
## Income exceeding Ksh 32,333 up to Ksh 800,000: Taxed at 30%
## Income above Ksh 800,000: Taxed at 35%

def get_payee(taxable_income, relief):
    payee=0
    if taxable_income>=0 and taxable_income<=24000:
        payee=0
    elif taxable_income>24000 and taxable_income<=32333:
        payee=(24000*0.1)+((taxable_income-24000)*0.25)
    
    elif taxable_income>32333 and taxable_income<=500000:
        payee=(24000*0.1)+(8333*0.25)+((taxable_income-32333)*0.30) - relief
    
    elif taxable_income>500000 and taxable_income<=800000:
        payee=(24000*0.1)+ (8333*0.25) +(467667*0.30)+((taxable_income-500000*0.325)) - relief
    
    else:
        taxable_income>800000 and taxable_income<=1600000
        payee=(24000*0.1)+ (8333*0.25) +(467667*0.30)  +(300000*0.325)+((taxable_income-800000*0.35))- relief
    

payee= get_payee(taxable_income)
print(f"PAYEE: {payee}")