import mysql.connector
from auth import Auth
from items import BakeryItem
from reports import Reports

def main():
    # Database Connection
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="shreya93@",
            database="bakery_management"
        )
        print("Connected to the database successfully.")
    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")
        return

    auth = Auth(db)
    items = BakeryItem(db)
    reports = Reports(db)

    user_role = None
    while True:
        print("\n--- Bakery Management ---")
        print("1. Register")
        print("2. Login")
        print("3. Add Item (Manager only)")
        print("4. Update Stock")
        print("5. Generate Sales Report")
        print("6. Display Inventory")
        print("7. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            # Register
            username = input("Username: ")
            password = input("Password: ")
            role = input("Role (cashier/manager): ").lower()
            auth.register(username, password, role)
            print("Registration complete.")

        elif choice == '2':
            # Login
            username = input("Username: ")
            password = input("Password: ")
            user_role = auth.login(username, password)
            if user_role:
                print(f"Login successful! You are logged in as a {user_role}.")
            else:
                print("Login failed.")

        elif choice == '3':
            # Add Item (Manager only)
            if user_role == 'manager':
                name = input("Item Name: ")
                price = float(input("Item Price: "))
                stock = int(input("Item Stock: "))
                items.add_to_db(name, price, stock)
            else:
                print("Access Denied: Only managers can add items.")

        elif choice == '4':
            # Update Stock
            if user_role:
                item_name = input("Item Name: ")
                quantity_sold = int(input("Quantity Sold: "))
                items.update_stock(item_name, quantity_sold)
            else:
                print("You must be logged in to update stock.")

        elif choice == '5':
            # Generate Sales Report
            if user_role:
                period = input("Enter report period (daily/weekly/monthly): ").lower()
                reports.generate_report(period)
            else:
                print("You must be logged in to generate reports.")

        elif choice == '6':
            # Display Inventory
            items.display_inventory()

        elif choice == '7':
            # Exit
            print("Exiting system. Goodbye!")
            db.close()
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
