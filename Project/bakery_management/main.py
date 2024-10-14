import mysql.connector
from auth import Auth
from items import BakeryItem
from reports import Reports


def main():
    # Database Connection
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="shreya93@",
        database="bakery_management"
    )

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
            username = input("Username: ")
            password = input("Password: ")
            role = input("Role (cashier/manager): ").lower()
            auth.register(username, password, role)

        elif choice == '2':
            username = input("Username: ")
            password = input("Password: ")
            user_role = auth.login(username, password)

        elif choice == '3':
            if user_role == 'manager':
                name = input("Item Name: ")
                price = float(input("Item Price: "))
                stock = int(input("Item Stock: "))
                items.add_to_db(name, price, stock)
            else:
                print("Access Denied: Only managers can add items.")

        elif choice == '4':
            item_name = input("Item Name: ")
            quantity_sold = int(input("Quantity Sold: "))
            items.update_stock(item_name, quantity_sold)

        elif choice == '5':
            period = input("Enter report period (daily/weekly/monthly): ").lower()
            reports.generate_report(period)

        elif choice == '6':
            items.display_inventory()

        elif choice == '7':
            print("Exiting system. Goodbye!")
            db.close()
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
