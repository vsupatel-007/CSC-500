price = float(input("Input charge for the food       --> "))
tip = price * .18
sales_tax = price * .07
total = price + tip + sales_tax
print("Amount with 18 percent tip      -->", round(tip , 2 ))
print("Amount with 7 percent sales tax -->",  round(sales_tax , 2) )
print("Total                           -->", round(total , 2) )