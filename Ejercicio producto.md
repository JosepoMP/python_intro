```python
inventory = {
    'rice': {"price": 20.0, "quantity": 3},
    'pear': {"price": 12.0, "quantity": 5},
    'apple': {"price": 11.0, "quantity": 2},
    'juice': {"price": 5.0, "quantity": 3},
    'oil': {"price": 10.0, "quantity": 4}
}

def add_product():
    name = input("Enter product name: ").lower()
    if name in inventory:
        print("Product already exists.")
        return
    try:
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
        if price > 0 and quantity >= 0:
            inventory[name] = {"price": price, "quantity": quantity}
            print(f"Product '{name}' added.")
        else:
            print("Price must be positive and quantity cannot be negative.")
    except ValueError:
        print("Invalid input.")

def view_product():
    name = input("Enter product name to search: ").lower()
    product = inventory.get(name)
    if product:
        print(f"{name.title()} - Price: {product['price']}, Quantity: {product['quantity']}")
    else:
        print("Product not found.")

def update_price():
    name = input("Enter product name to update price: ").lower()
    if name in inventory:
        try:
            new_price = float(input("Enter new price: "))
            if new_price > 0:
                inventory[name]["price"] = new_price
                print(f"Price of '{name}' updated.")
            else:
                print("Price must be positive.")
        except ValueError:
            print("Invalid input.")
    else:
        print("Product not found.")

def delete_product():
    name = input("Enter product name to delete: ").lower()
    if name in inventory:
        confirm = input(f"Are you sure you want to delete '{name}'? (yes/no): ").lower()
        if confirm == "yes":
            del inventory[name]
            print(f"Product '{name}' deleted.")
    else:
        print("Product not found.")

def calculate_total_value():
    total = sum(p["price"] * p["quantity"] for p in inventory.values())
    print(f"Total inventory value: {total}")

def show_menu():
    print("\n--- Inventory Menu ---")
    print("1. Add product")
    print("2. View product")
    print("3. Update product price")
    print("4. Delete product")
    print("5. Calculate total inventory value")
    print("6. Exit")

def main():
    while True:
        show_menu()
        option = input("Choose an option (1-6): ")
        if option == "1":
            add_product()
        elif option == "2":
            view_product()
        elif option == "3":
            update_price()
        elif option == "4":
            delete_product()
        elif option == "5":
            calculate_total_value()
        elif option == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
```
Perfecto. Aquí tienes un archivo README.md listo para tu proyecto:


---

README.md

# Inventory Management System

## Description

This Python program is a simple command-line inventory management system. It allows users to:

- Add products to the inventory
- View information about a specific product
- Update the price of a product
- Delete a product from the inventory (with confirmation)
- Calculate and display the total value of the inventory

The program starts with 5 preloaded products and uses a menu-based interface for user interaction.

## Initial Inventory

```python
    
inventory = {
    'rice': {"price": 20.0, "quantity": 3},
    'pear': {"price": 12.0, "quantity": 5},
    'apple': {"price": 11.0, "quantity": 2},
    'juice': {"price": 5.0, "quantity": 3},
    'oil': {"price": 10.0, "quantity": 4}
}

Requirements

Python 3.x


How to Run

1. Make sure you have Python 3 installed.


2. Download the inventario.py file.


3. Open a terminal and navigate to the folder where the file is located.


4. Run the program with:



python inventario.py

Sample Usage

Example 1: Add Product

Enter product name: milk
Enter product price: 15.0
Enter product quantity: 6
Product 'milk' added.

Example 2: View Product

Enter product name to search: rice
Rice - Price: 20.0, Quantity: 3

Example 3: Update Price

Enter product name to update price: oil


