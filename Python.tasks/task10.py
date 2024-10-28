# Write a program that calculates the total stock in a company from the array/list below if we know that the stock is the last digit in every array/list.

prods = [['omo','30Kshs','300'], ['milk','50Kshs','200'],['bread','45Kshs','359'], ['coffee','5Kshs','79']]


# sum = int(prods[0][2])+int(prods[1][2])+int(prods[2][2])+int(prods[3][2])
# print(sum)
    
for i in prods:
        stock = prods[2]
        prods += int(stock)


# Example usage
prods = [['omo', '30Kshs', '300'], ['milk', '50Kshs', '200'], ['bread', '45Kshs', '359'], ['coffee', '5Kshs', '79']]
total_stock = calculate_total_stock(prods)
print(f"The total stock is: {total_stock}")


