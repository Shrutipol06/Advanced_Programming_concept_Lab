inventory = {}


# Function to add a product
def add_product():
    name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))

    inventory[name] = quantity

    print("Product added successfully.")


# Function to update product quantity
def update_product():
    name = input("Enter product name: ")

    if name in inventory:
        quantity = int(input("Enter new quantity: "))
        inventory[name] = quantity
        print("Quantity updated successfully.")
    else:
        print("Product not found.")


# Function to remove product
def remove_product():
    name = input("Enter product name: ")

    if name in inventory:
        if inventory[name] == 0:
            del inventory[name]
            print("Product removed successfully.")
        else:
            print("Product quantity is not zero.")
    else:
        print("Product not found.")


# Function to find product with highest stock
def highest_stock():
    if len(inventory) == 0:
        print("Inventory is empty.")
        return

    highest_product = ""
    highest_quantity = 0

    for product in inventory:
        if inventory[product] > highest_quantity:
            highest_quantity = inventory[product]
            highest_product = product

    print("Product with highest stock:", highest_product)
    print("Quantity:", highest_quantity)


# Function to display total unique products
def total_products():
    count = 0

    for product in inventory:
        count += 1

    print("Total unique products:", count)


# Display inventory
def display_inventory():
    print("\nInventory:")

    for product in inventory:
        print(product, ":", inventory[product])


# Main program
while True:
    print("\n--- Inventory Management System ---")
    print("1. Add Product")
    print("2. Update Product")
    print("3. Remove Product")
    print("4. Highest Stock")
    print("5. Total Products")
    print("6. Display Inventory")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        update_product()

    elif choice == "3":
        remove_product()

    elif choice == "4":
        highest_stock()

    elif choice == "5":
        total_products()

    elif choice == "6":
        display_inventory()

    elif choice == "7":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")