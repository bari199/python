# Cart system using dictionary, functions, loops, and if-else

cart = {}

# Function to add item
def add_item(cart):
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    quantity = int(input("Enter quantity: "))

    if name in cart:
        cart[name]["quantity"] += quantity
    else:
        cart[name] = {"price": price, "quantity": quantity}

    print("Item added to cart successfully!\n")


# Function to remove item
def remove_item(cart):
    name = input("Enter item name to remove: ")

    if name in cart:
        del cart[name]
        print("Item removed successfully!\n")
    else:
        print("Item not found in cart!\n")


# Function to view cart
def view_cart(cart):
    if not cart:
        print("Cart is empty!\n")
        return

    print("\nYour Cart:")
    print("Item\tPrice\tQuantity\tTotal")
    for item, details in cart.items():
        total = details["price"] * details["quantity"]
        print(f"{item}\t{details['price']}\t{details['quantity']}\t\t{total}")
    print()


# Function to calculate total price
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
        view_cart(cart)
    elif choice == "4":
        total_price(cart)
    elif choice == "5":
        print("Thank you for shopping!")
        break
    else:
        print("Invalid choice! Please try again.\n")
