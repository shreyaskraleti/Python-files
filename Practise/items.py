class BakeryItem:
    def __init__(self, db):
        self.db = db
        self.cursor = db.cursor()

    def add_to_db(self, name, price, stock):
        # Fixed the missing line break
        sql = "INSERT INTO inventory (item_name, price, stock) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, (name, price, stock))
        self.db.commit()
        print(f"Item '{name}' added to inventory.")

    def update_stock(self, item_name, quantity_sold):
        # Check if the item exists
        sql_check = "SELECT stock, price FROM inventory WHERE item_name = %s"
        self.cursor.execute(sql_check, (item_name,))
        item = self.cursor.fetchone()

        if item:
            current_stock, price = item
            if current_stock >= quantity_sold:
                # Update stock in inventory
                sql_update = "UPDATE inventory SET stock = stock - %s WHERE item_name = %s"
                self.cursor.execute(sql_update, (quantity_sold, item_name))
                
                # Record the sale in the sales table
                sql_sales = """
                INSERT INTO sales (item_id, quantity_sold, total_price)
                VALUES ((SELECT item_id FROM inventory WHERE item_name = %s), %s, %s)
                """
                total_price = price * quantity_sold
                self.cursor.execute(sql_sales, (item_name, quantity_sold, total_price))
                self.db.commit()

                print(f"Stock updated for {item_name}.")
            else:
                print(f"Not enough stock for {item_name}. Available stock: {current_stock}")
        else:
            print(f"Item '{item_name}' not found.")

    def display_inventory(self):
        sql = "SELECT * FROM inventory"
        self.cursor.execute(sql)
        items = self.cursor.fetchall()
        print("--- Inventory ---")
        for item in items:
            print(f"Item ID: {item[0]}, Name: {item[1]}, Price: ${item[2]:.2f}, Stock: {item[3]}")
