import mysql.connector

class BakeryItem:
    def __init__(self, db):
        self.db = db
        self.cursor = db.cursor()

    def add_to_db(self, name, price, stock):
        try:
            # Clear any unread results before executing a new query
            self.cursor.reset()

            sql = "INSERT INTO items (name, price, stock) VALUES (%s, %s, %s)"
            self.cursor.execute(sql, (name, price, stock))
            self.db.commit()
            print(f"Item {name} added successfully.")
        
        except mysql.connector.errors.InternalError as err:
            print(f"InternalError occurred: {err}")
        
        except mysql.connector.Error as err:
            print(f"Error adding item: {err}")

    def update_stock(self, name, quantity_sold):
        try:
            # Clear any unread results before executing a new query
            self.cursor.reset()

            sql = "UPDATE items SET stock = stock - %s WHERE name = %s"
            self.cursor.execute(sql, (quantity_sold, name))
            self.db.commit()
            print(f"Stock for {name} updated successfully.")
        
        except mysql.connector.errors.InternalError as err:
            print(f"InternalError occurred: {err}")
        
        except mysql.connector.Error as err:
            print(f"Error updating stock: {err}")

    def display_inventory(self):
        try:
            # Clear any unread results before executing a new query
            self.cursor.reset()

            sql = "SELECT * FROM items"
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            print("Current Inventory:")
            for row in result:
                print(row)
        
        except mysql.connector.errors.InternalError as err:
            print(f"InternalError occurred: {err}")
        
        except mysql.connector.Error as err:
            print(f"Error displaying inventory: {err}")
