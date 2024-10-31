# Write a program that calculates the total stock in a company from the array/list below if we know that the stock is the last digit in every array/list.

prods = [['omo','30Kshs','300'], ['milk','50Kshs','200'],['bread','45Kshs','359'], ['coffee','5Kshs','79']]


prods = [['omo','30Kshs','300'], ['milk','50Kshs','200'],['bread','45Kshs','359'], ['coffee','5Kshs','79']]

total_stock = 0

for prod in prods:
    stock = int(prod[-1])
    total_stock += stock

print(f"Total stock is: {total_stock}")

