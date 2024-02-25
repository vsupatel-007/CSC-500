def calculate_cost(item_price, item_quantity):
  # method that will multipy item_price * item_quantity.
  return item_price * item_quantity


class ItemToPurchase():
  # a class that will have item_name, item_price, item_quantity variable.
  item_name = ''
  item_price = 0.0
  item_quantity = 0
  item_description = "none"
  def __init__(self):
    # default constructor that will set all the variable to 0 or "none."
    self.item_name = "none"
    self.item_price = 0
    self.item_quantity = 0
    self.item_description = "none"

  def print_item_cost(self):
    # method which will calculate the total of the current item.
    print(self.item_name, self.item_quantity, "@", "$" + str(self.item_price), "=", "$"+str(self.item_price * self.item_quantity))


class ShoppingCart():
  def __init__(self):
    self.customer_name = "none"
    self.date = "January 1, 2020"
    self.cart_items = []

  def add_item(self, item_to_purchase):
    self.cart_items.append(item_to_purchase)

  def remove_item(self, item_name):
    flag = False
    counter = 0
    for item in self.cart_items:
      if item.item_name == item_name:
        flag = True
        temp = self.cart_items.pop(counter)
      counter +=1

    if not flag:
       print("Item not found in cart. Nothing Removed.")


  def modify_item(self, item_to_purchase):
    flag = False
    for i in range(len(self.cart_items)):
      if self.cart_items[i].item_name == item_to_purchase.item_name:
        flag = True
        self.cart_items[i].item_quantity = item_to_purchase.item_quantity

    if not flag:
       print("Item not found in cart. Nothing modified.")

  def get_num_items_in_cart(self):
    sum = 0
    for item in self.cart_items:
      sum += item.item_quantity
    return sum

  def get_cost_of_cart(self):
    sum = 0
    for item in self.cart_items:
      sum += calculate_cost(item.item_price, item.item_quantity)
    return sum

  def print_total(self):
    if len(self.cart_items) == 0:
      print("\t SHOPPING CART IS EMPTY")

    else:
      print()
      print(self.customer_name + "'s", "Shopping Cart -", self.date)
      print("\t Number of Items:", self.get_num_items_in_cart())

      for item in self.cart_items:
        item.print_item_cost()
      print("\t Total: $"+str(round(self.get_cost_of_cart(), 2) ))

  def print_description(self):
    print(self.customer_name + "'s", "Shopping Cart -", self.date)
    print("\t Item Descriptions")
    for item in self.cart_items:
      print(item.item_name+":", item.item_description)

def print_menu():
  print("")
  print("\t MENU")
  print("a - Add item to card")
  print("r - Remove item from cart")
  print("c - Change item quantity")
  print("i - Output items' descriptions")
  print("o - Output shopping cart")
  print("q - Quit")
  print("Choose an option: ", end="")

def menu_functionality(cart, character_input):
  if character_input == "a":
    item = ItemToPurchase()
    item.item_name = str(input("Enter the item name: "))
    item.item_price = float(input("Enter the item price: $"))
    item.item_quantity = int(input("Enter the item quantity: "))
    item.item_description = str(input("Enter the item description: "))
    # cart.cart_items.append(item)
    cart.add_item(item)

  elif character_input == "r":
    print("\t OUTPUT SHOPPING CART")
    item_name = str(input("Enter the item name to be removed from the cart: "))
    cart.remove_item(item_name)

  elif character_input == "c":
    print("\t Change Item Quantity")
    item = ItemToPurchase()
    item.item_name = str(input("Enter the item name that needs quantity updated: "))
    item.item_quantity = int(input("Enter the item quantity: "))
    cart.modify_item(item)

  elif character_input == "i":
    print("\t OUTPUT ITEMS' DESCRIPTIONS")
    cart.print_description()

  elif character_input == "o":
    print("\t OUTPUT SHOPPING CART")
    cart.print_total()

character_input = ""
cart_class = ShoppingCart()
cart_class.customer_name = str(input("Enter your name --> "))
cart_class.date = str(input("Enter date --> "))


while character_input != "q":
  print_menu()
  character_input = str(input(""))
  print("")
  if character_input == "a" or character_input == "r" or character_input == "c" or character_input == "i" or character_input == "o":
    menu_functionality(cart_class, character_input)

  elif character_input == "q":
    break

  else:
    print("Invalid input. Try again.")
