cart ={}
# Add items 
def add_item(cart):
    name = input("Enter item name:")
    price = float(input("Enter the item price:"))
    quantity = int(input("Enter the quantity:"))

    if name in cart:
        cart[name]["quantity"] += quantity
    else:
        cart[name]={"price":price,"quantity":quantity}
    print("Item added successfully !\n")



# Removes items 
def remove_item(cart):
    name = input("Enter item name for remove: ")

    if name in cart:
        del cart[name]
        print("Item remove successfully:! \n")
    else:
        print("Item is not found \n")


# View items
def view_item(cart):
    if not cart:
        print("Cart is empty\n")
        return
    print("\n Your Cart: ")

print("Item\tPrice\tQunatity\tTotal")
for item, details in cart.items():
    total = details["price"] * details["quantity"]
    print(f"{item}\t{details['price']}\t{details['quantity']}\t\t{total}")
print()


#Total price 

def total_price(cart):
    total = 0
    for details in cart.values():
        total += details["price"] * details["quantity"]

    print(f"Total Cart Price: {total}\n")

# Main menu loop
while True:
    print("------ CART MENU ------")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Cart")
    print("4. Total Price")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_item(cart)
    elif choice == "2":
        remove_item(cart)
    elif choice == "3":
        view_item(cart)
    elif choice == "4":
        total_price(cart)
    elif choice == "5":
        print("Thank you for shopping!")
        break
    else:
        print("Invalid choice! Please try again.\n")
