class ItemToPurchase():
  # a class that will have item_name, item_price, item_quantity variable.
  item_name = ''
  item_price = 0.0
  item_quantity = 0
  def __init__(self):
    # default constructor that will set all the variable to 0 or "none."
    self.item_name = "none"
    self.item_price = 0
    self.item_quantity = 0

  def print_item_cost(self):
    # method which will calculate the total of the current item.
    print(self.item_name, self.item_quantity, "@", "$" + str(self.item_price), "=", "$"+str(self.item_price * self.item_quantity))

def calculate_cost(item_price, item_quantity):
  # method that will multipy item_price * item_quantity.
  return item_price * item_quantity

item_list = []
for i in range(1,3):
  print("\t\t", "Item", i)
  item = ItemToPurchase() # creating new instance of the calass
  item.item_name = str(input("Enter the item name: ")) # assigning the item name 
  item.item_price = float(input("Enter the item price:$")) # assining the item price
  item.item_quantity = int(input("Enter the item quantity: ")) # assining the item quantity
  item_list.append(item) # adding the object to the list 
  item.print_item_cost() # printing the item's cost using the methond inside the class
  print()

# outputing the total cost of item 1 and item 2
print("\t\t TOTAL COST")
print(item_list[0].item_name, item_list[0].item_quantity, "@", "$"+str(item_list[0].item_price), "=", "$"+ str(calculate_cost(item_list[0].item_price, item_list[0].item_quantity) ))
print(item_list[1].item_name, item_list[1].item_quantity, "@", "$"+str(item_list[1].item_price), "=", "$"+ str(calculate_cost(item_list[1].item_price, item_list[1].item_quantity) ))
print("Total:", "$"+str( calculate_cost(item_list[0].item_price, item_list[0].item_quantity) + calculate_cost(item_list[1].item_price, item_list[1].item_quantity) ))