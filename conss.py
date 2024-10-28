# write a program that
# takes users credit score and annual income as input
# if the credit score is above 700, check if the income is above $50000
# if both conditions are met, print "loan approved"
# if only the credit score is high, print "Income requirement not met"
# if credit score is below 700, print "Credit score too low"
           

credit_score= (int(input("Enter your credit score: ")))
annual_income= (float(input("Enter your annual income: ")))

if credit_score >700:

    if annual_income > 50000:
        print("loan approved")

    else:
        print("Income requirement not met")  

else:
    print("Credit score too low")          