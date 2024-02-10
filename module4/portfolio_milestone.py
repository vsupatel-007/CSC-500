class ItemToPurchase():
  item_name = ''
  item_price = 0.0
  item_quantity = 0
  def __init__(self):
    self.item_name = "none"
    self.item_price = 0
    self.item_quantity = 0

  def print_item_cost(self):
    print(self.item_name, self.item_quantity, "@", "$" + str(self.item_price), "=", "$"+str(self.item_price * self.item_quantity))

def calculate_cost(item_price, item_quantity):
  return item_price * item_quantity

item_list = []
for i in range(1,3):
  print("\t\t", "Item", i)
  item = ItemToPurchase()
  item.item_name = str(input("Enter the item name: "))
  item.item_price = float(input("Enter the item price:$"))
  item.item_quantity = int(input("Enter the item quantity: "))
  item_list.append(item)
  item.print_item_cost()
  print()

print("\t\t TOTAL COST")
print(item_list[0].item_name, item_list[0].item_quantity, "@", "$"+str(item_list[0].item_price), "=", "$"+ str(calculate_cost(item_list[0].item_price, item_list[0].item_quantity) ))
print(item_list[1].item_name, item_list[1].item_quantity, "@", "$"+str(item_list[1].item_price), "=", "$"+ str(calculate_cost(item_list[1].item_price, item_list[1].item_quantity) ))
print("Total:", "$"+str( calculate_cost(item_list[0].item_price, item_list[0].item_quantity) + calculate_cost(item_list[1].item_price, item_list[1].item_quantity) ))