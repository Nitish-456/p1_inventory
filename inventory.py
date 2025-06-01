import os
import csv
from datetime import datetime

FILENAME = "Inventory.csv"
LOG_FILE = "Record.txt"

# Create CSV file if it doesn't exist
if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Product", "Price", "Quantity"])


def log_action(action, details):
    with open(LOG_FILE, "a") as log:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"[{timestamp}] {action}: {details}\n")


def add_product():
    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)

        while True:
            name = input(
                "Enter the product name (or type 'exit' to stop): ").strip()
            if name.lower() == "exit":
                break

            while True:
                try:
                    price = float(
                        input("Enter the price of Product: ").strip())
                    if price < 0:
                        print("Price cannot be negative! Enter a valid price.")
                        continue
                    break
                except ValueError:
                    print("Invalid Input! Please enter a numeric value for price.")

            while True:
                try:
                    quantity = int(
                        input("Enter the Quantity of Product: ").strip())
                    if quantity < 0:
                        print("Quantity cannot be negative! Enter a valid quantity.")
                        continue
                    break
                except ValueError:
                    print("Invalid Quantity! Please enter a numeric value.")

            writer.writerow([name, price, quantity])
            print(f"Product '{name}' added successfully!\n")
            log_action(
                "ADD", f"Product: {name}, Price: {price}, Quantity: {quantity}")


def view_products():
    with open(FILENAME, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        print("\nCurrent Inventory:")
        for row in reader:
            print(f"Product: {row[0]}, Price: {row[1]}, Quantity: {row[2]}")
    print()


def update_product():
    product_to_update = input("Enter the product name to update: ").strip()
    new_data = []
    updated = False

    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0].strip().lower() == product_to_update.lower():
                print(f"Current Product Details: {row}")

                while True:
                    try:
                        new_price = float(input("Enter new price: ").strip())
                        if new_price < 0:
                            print("Price cannot be negative!")
                            continue
                        break
                    except ValueError:
                        print("Invalid input! Enter a numeric value for price.")

                while True:
                    try:
                        new_quantity = int(
                            input("Enter new quantity: ").strip())
                        if new_quantity < 0:
                            print("Quantity cannot be negative!")
                            continue
                        break
                    except ValueError:
                        print("Invalid input! Enter a numeric value for quantity.")

                new_data.append([row[0], new_price, new_quantity])
                updated = True
                log_action(
                    "UPDATE", f"Product: {row[0]}, New Price: {new_price}, New Quantity: {new_quantity}")
            else:
                new_data.append(row)

    if updated:
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(new_data)
        print("Product updated successfully!\n")
    else:
        print("Product not found!\n")
        log_action(
            "UPDATE", f"Attempted to update {product_to_update}, but product was not found.")


def delete_product():
    product_to_delete = input(
        "Enter the product name to delete: ").strip().lower()
    new_data = []
    deleted = False

    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0].strip().lower() != product_to_delete:
                new_data.append(row)
            else:
                deleted = True
                log_action(
                    "DELETE", f"Product deleted: {row[0]}, Price: {row[1]}, Quantity: {row[2]}")

    if deleted:
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(new_data)
        print(f"Product '{product_to_delete}' deleted successfully!\n")
    else:
        print("Product not found!\n")
        log_action(
            "DELETE", f"Attempted to delete {product_to_delete}, but product was not found.")


def search_product():
    print("\nSearch Options:")
    print("1. Search by Product Name")
    print("2. Search by Price Range")
    print("3. Search by Quantity")

    choice = input("Enter your choice (1-3): ").strip()

    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        next(reader)
        results = []

        if choice == "1":
            search_name = input(
                "Enter the product name or part of it: ").strip().lower()
            results = [
                row for row in reader if search_name in row[0].strip().lower()]
        elif choice == "2":
            min_price = float(input("Enter minimum price: ").strip())
            max_price = float(input("Enter maximum price: ").strip())
            results = [row for row in reader if min_price <=
                       float(row[1]) <= max_price]
        elif choice == "3":
            search_quantity = int(input("Enter minimum quantity: ").strip())
            results = [row for row in reader if int(row[2]) >= search_quantity]
        else:
            print("Invalid choice! Please enter a valid option.")
            return

    if results:
        print("\nSearch Results:")
        for row in results:
            print(f"Product: {row[0]}, Price: {row[1]}, Quantity: {row[2]}")
        log_action("SEARCH", f"Search results found for choice {choice}")
    else:
        print("No matching products found!")
        log_action("SEARCH", f"No results found for choice {choice}")


while True:
    print("------ Product Inventory Manager ------")
    print("1. Add Product")
    print("2. View Products")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Search Product")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ").strip()
    if choice == "1":
        add_product()
    elif choice == "2":
        view_products()
    elif choice == "3":
        update_product()
    elif choice == "4":
        delete_product()
    elif choice == "5":
        search_product()
    elif choice == "6":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.\n")
