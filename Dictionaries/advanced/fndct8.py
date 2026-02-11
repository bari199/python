cart={}

# Function to add product with detailed attributes
def add_product(cart):
    username = input("Enter your username: ")
    product_name = input("Enter product name: ") 
    product_size = input("Enter product size: ")
    product_color = input("Enter product color: ")
    gender = input("Enter gender (M/F/U): ")
    product_quantity = int(input("Enter product quantity: "))                                                        
    product_price = float(input("Enter product price: "))

    if product_name in cart:
        cart[product_name]["product_quantity"] += product_quantity
    else:
        cart[product_name] = {
            "username":username,
            "product_price":product_price,
            "product_size":product_size,
            "product_color":product_color,
            "gender":gender,
            "product_quantity":product_quantity
        }
    print("Item added to cart successfully!\n")

def remove_product(cart):
    product_name = input("Enter product name to remove: ")

    if product_name in cart:
        del cart[product_name]
        print("Item removed successfully!\n")
    else:
        print("Item not found in cart!\n")
    
def view_cart(cart):
    if not cart:
        print("Cart is empty!\n")
        return
    print("\nYour Cart:")
    print("User\t\tProduct\t\tPrice\t\tSize\t\tColor\t\tGender\t\tQuantity\t\tTotal")
    for item, details in cart.items():
        total = details["product_price"] * details["product_quantity"]
        print( f"{details['username']}\t{item}\t{details['product_price']}\t"
            f"{details['product_size']}\t{details['product_color']}\t"
            f"{details['gender']}\t{details['product_quantity']}\t{total}")  
    print()


def total_price(cart):
    total = 0
    for details in cart.values():
        total += details["product_price"] * details["product_quantity"]
    print(f"Total Cart Price: {total}\n")

while True:
    print("------ CART MENU ------")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. View Cart")
    print("4. Total Price")
    print("5. Exit")

    choice = input("Enter your choice: ")
    if choice == '1':
        add_product(cart)
    elif choice == '2':
        remove_product(cart)
    elif choice == '3':
        view_cart(cart)
    elif choice == '4':
        total_price(cart)
    elif choice == '5':
        print("Exiting the cart. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.\n")
