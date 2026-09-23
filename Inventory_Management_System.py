inventory = {}

while True:
    print("\n--- INVENTORY MANAGEMENT SYSTEM ---")
    print("1. Add Item (Create)")
    print("2. View Inventory (Read)")
    print("3. Update Item (Update)")
    print("4. Delete Item (Delete)")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")

    # 1. CREATE
    if choice == '1':
        item_id = input("Enter Item ID: ")
        if item_id in inventory:
            print("Error: Item ID already exists!")
        else:
            name = input("Enter Item Name: ")
            price = float(input("Enter Item Price: "))
            qty = int(input("Enter Item Quantity: "))
            inventory[item_id] = {"name": name, "price": price, "quantity": qty}
            print(f"'{name}' added successfully!")

    # 2. READ
    elif choice == '2':
        if not inventory:
            print("Inventory is empty.")
        else:
            print("\nID\tName\t\tPrice\tQuantity")
            print("-" * 40)
            for item_id, details in inventory.items():
                print(f"{item_id}\t{details['name']}\t\tRs.{details['price']:.2f}\t{details['quantity']}")

    # 3. UPDATE
    elif choice == '3':
        item_id = input("Enter Item ID to update: ")
        if item_id in inventory:
            print("1. Update Price\n2. Update Quantity")
            sub_choice = input("Enter choice: ")
            if sub_choice == '1':
                new_price = float(input("Enter new price: "))
                inventory[item_id]['price'] = new_price
                print("Price updated.")
            elif sub_choice == '2':
                new_qty = int(input("Enter new quantity: "))
                inventory[item_id]['quantity'] = new_qty
                print("Quantity updated.")
            else:
                print("Invalid sub-choice.")
        else:
            print("Item not found.")

    # 4. DELETE
    elif choice == '4':
        item_id = input("Enter Item ID to delete: ")
        if item_id in inventory:
            deleted_name = inventory[item_id]['name']
            del inventory[item_id]
            print(f"Item '{deleted_name}' removed from inventory.")
        else:
            print("Item not found.")

    # 5. EXIT
    elif choice == '5':
        print("Exiting Inventory System. Thank you!")
        break

    else:
        print("Invalid choice! Please choose between 1 and 5.")