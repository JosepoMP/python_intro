```python
inventory = {
    'rice': {"price": 20.0, "quantity": 2},
    'apple': {"price": 15.0, "quantity": 5},
    'juice': {"price": 5.0, "quantity": 2},
    'oil': {"price": 19.0, "quantity": 3},
    'pear': {"price": 10.0, "quantity": 4}

}

# add any product 
# This is one of the main options of the program, it allows the user to add any new product he wants.



def add_product():
    name = input("Please, Enter product name: ").lower()
    if name in inventory:
        print(" This product already exists. ")
        return
    try:
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
        if price > 0 and quantity >= 0:
            inventory[name] = {"price": price, "quantity": quantity}
            print(f"✅ The product '{name}' was added correclty. ")
        else:
            print("⚠️ Price must be postivie and quantity cannot be negative. ")
    except ValueError:
        print(" ❌ Invalid Option, try again.")
        return


# consult products in inventory 
# The user will be able to see all the products they have stored, also, check prices, quantities, etc... 
# This will make it easier for the user to be able to select a specific product.

def consult_product():
    if not inventory:
        print("Inventory is empty. ")
        return
    
    print("\n --- Current Inventory ---")
    print(f"{'product':<10} {'price':>10} {'quantity':>10}")
    print("-" * 32)
    for name, info in inventory.items():
        print(f"{name:<10} {info['price']:>10.2f} {info['quantity']:>10}")

    name = input("📋 Enter product name you want to consult: ").lower()
    product = inventory.get(name)
    if product:
        print(f"{name.title()} - Price: {product['price']}, Quantity: {product['quantity']}")
    else:
        print("⚠️ Product not found. ")
        
    
# modify price of a product 
# This part of the code allows the user to update the information of any product at any time.



def update_price():
    name = input("Enter the name of the product you want to be updated: ").lower()
    if name in inventory:
        try: 
            new_price = float(input("Enter new price: "))
            if new_price > 0:
                inventory[name]["Price"] = new_price
                print(f"✅ Price of '{name}' updated successfully. ")
            else: 
                print("⚠️ Price must be a positive number. ")
        except ValueError:
            print(" ❌ Invalid Option, Try again.")
    else:
        print("⚠️ Product not found. ")
        return

# Delete any product of the inventory :
# The user can delete any product from the inventory whenever he wants, obviously a confirmation will be sent to the user to avoid involuntary deletions.

def delete_product():
    name = input("Enter the product name you want to delete: ").lower()
    if name in inventory:
        confirm = input(f"🔴 Are you sure that you want to delete '{name}'? (yes/no): ").lower()
        if confirm == "yes":
            del inventory[name]
            print(f"🗑️ Product '{name}' deleted.")

    else:
        print("Product was not found. ")
        return
    


# Now, Calculate the total value of the products :
# We need to make a mathematical function with logical operators so that the user can see the total value of the products in their inventory.

def total_value():
        total = sum(p["price"] * p["quantity"] for p in inventory.values())
        print(f"💰 The total inventory value: {total}")



# Principal menu : 
# Here we have the part of the code that will allow the user to see an organized interface and select the desired options.



def show_menu():
    print("\n --- Inventory Menu --- ")
    print("1. 📎 Add product. ")
    print("2. 🗂️ Consult product. ")    
    print("3. ⚙️ Update product price. ")
    print("4. 🗑️ Delete prduct. ")
    print("5. 💰 Calculate total inventory value. ")
    print("6. 👋 Exit.")

def main():
    while True:
        show_menu()
        option = input("Please, Choose an option (1-6): ")
        if option == "1":
            add_product()
        elif option == "2":
            consult_product()
        elif option == "3":
            update_price()
        elif option == "4":
            delete_product()
        elif option == "5":
            total_value()
        elif option == "6":
            print("Exiting the program. ")
            break
        else:
            print("Invalid option, try again. ")


if __name__ == "__main__":
    main()
```

# This python program is a simple inventory management system. The system allows user to:
    #  - Add products to the inventory in a simple way.
    #  - Review information about a specific product.
    #  - Update the price of any previously registered product.
    #  - Dele a product form the inventory with confirmation.
    #  - Calculate and display the total value of the inventory. 

# Simple usage 

# Explame 1: Add a product
    Enter product name: Milk
    enter product price: 15.0
    Enter product quantity: 6
    Product 'milk' added correclty. 

# Example 2: View Product
    Enter product name to search: rice
    Rice - Price: 20.0, Quantity: 3

# Example 3: update price 

    Enter product name to update price: oil
    Enter new price: 12
    Price of 'oil' updated.

# Example 4: Delete Product

    Enter product name to delete: juice
    Are you sure you want to delete 'juice'? (yes/no): yes
    roduct 'juice' deleted.
