menu={
 'Pizza' : 400,
 'Burger':99,
 'Pasta':49,
 'Cold-cofee':89,
 'chocolate-shake':120
}
print("Welcome to our Python Restraurant")
print("Choose any item from the menu and make order")
for key,value in menu.items():
 print(f"{key}:{value}")

total_order = 0
item_1 = input("Enter Your order: ")
if item_1 in menu:
 total_order += menu[item_1]
 print(f"Your ordered item {item_1} went to prepare, Thank You")

else:
 print("Your ordered item is not available yet")

another_item = input("Do you want to make something else (Yes/No) ")
if another_item == "yes":
 item_2 = input("Enter another order: ")
 if item_2 in menu:
  total_order += menu[item_2]
  print(f"{item_2} is added in your list, Thank you")
 else:
  print(f"Your ordered item {item_2} is not available yet...")

print(f"Your total payment is {total_order}")

 