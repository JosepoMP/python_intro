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
    print(f"Total inventory value: ${total:.2f}")

def show_all_products():
    if not inventory:
        print("Inventory is empty.")
        return

    print("\n--- Current Inventory ---")
    print(f"{'Product':<10} {'Price':>10} {'Quantity':>10}")
    print("-" * 32)
    for name, info in inventory.items():
        print(f"{name:<10} {info['price']:>10.2f} {info['quantity']:>10}")

def show_menu():
    print("\n--- Inventory Menu ---")
    print("1. Add product")
    print("2. View product")
    print("3. Update product price")
    print("4. Delete product")
    print("5. Calculate total inventory value")
    print("6. Show all products")
    print("7. Exit")

def main():
    while True:
        show_menu()
        option = input("Choose an option (1-7): ")
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
            show_all_products()
        elif option == "7":
            print("Exiting program.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
```

---

Archivo: README.md

# Inventory Management System

## Description

This Python program is a simple command-line inventory management system. It allows users to:

- Add products to the inventory
- View information about a specific product
- Update the price of a product
- Delete a product from the inventory (with confirmation)
- Calculate and display the total value of the inventory
- Display all products in a well-formatted list

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


2. Save the inventario.py file.


3. Open a terminal and navigate to the folder where the file is located.


4. Run the program with:



python inventario.py

Sample Usage

Example: Add Product

Enter product name: milk
Enter product price: 15.0
Enter product quantity: 6
Product 'milk' added.

Example: View Product

Enter product name to search: rice
Rice - Price: 20.0, Quantity: 3

Example: Update Price

Enter product name to update price: oil
Enter new price: 12
Price of 'oil' updated.

Example: Delete Product

Enter product name to delete: juice
Are you sure you want to delete 'juice'? (yes/no): yes
Product 'juice' deleted.

Example: Show All Products

--- Current Inventory ---
Product         Price   Quantity
--------------------------------
rice            20.00          3
pear            12.00          5
apple           11.00          2
juice            5.00          3
oil             10.00          4

Example: Calculate Total Inventory Value

Total inventory value: $281.00

Author

Your Name
Course: [Course Name]
Date: [Submission Date]

---

¿Quieres que traduzca el `README.md` al español o lo dejamos completamente en inglés como lo exige el ejercicio?

