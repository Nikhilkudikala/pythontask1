# grocery_inventory_management.py

# Define the initial inventory as a dictionary
inventory = {}

def add_item():
    item_name = input("Enter the name of the item: ")
    quantity = int(input("Enter the quantity of the item: "))
    price = float(input("Enter the price of the item: "))
    
    # Add the item to the inventory
    inventory[item_name] = {"quantity": quantity, "price": price}
    print(f"{item_name} added to the inventory.")

def update_quantity():
    item_name = input("Enter the name of the item to update: ")
    if item_name in inventory:
        new_quantity = int(input("Enter the new quantity: "))
        inventory[item_name]["quantity"] = new_quantity
        print(f"Quantity for {item_name} updated to {new_quantity}.")
    else:
        print(f"{item_name} not found in the inventory.")

def view_inventory():
    print("\nCurrent Inventory:")
    for item_name, item_info in inventory.items():
        print(f"{item_name}: Quantity - {item_info['quantity']}, Price - ${item_info['price']}")

def remove_item():
    item_name = input("Enter the name of the item to remove: ")
    if item_name in inventory:
        del inventory[item_name]
        print(f"{item_name} removed from the inventory.")
    else:
        print(f"{item_name} not found in the inventory.")

def main():
    while True:
        print("\nGrocery Store Inventory Management")
        print("1. Add new item")
        print("2. Update item quantity")
        print("3. View inventory")
        print("4. Remove item")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_item()
        elif choice == "2":
            update_quantity()
        elif choice == "3":
            view_inventory()
        elif choice == "4":
            remove_item()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()






