class Reports:
    def __init__(self, db):
        self.db = db
        self.cursor = db.cursor()

    def add_sale(self, item_name, quantity, price):
        sql = "INSERT INTO sales (item_id, quantity_sold, total_price) VALUES ((SELECT item_id FROM inventory WHERE item_name = %s), %s, %s)"
        self.cursor.execute(sql, (item_name, quantity, price * quantity))
        self.db.commit()
        print(f"Sale recorded: {quantity} of {item_name} sold.")

    def generate_report(self, period):
        if period == 'daily':
            sql = "SELECT item_name, quantity_sold, total_price FROM sales JOIN inventory ON sales.item_id = inventory.item_id WHERE DATE(sale_date) = CURDATE()"
        elif period == 'weekly':
            sql = "SELECT item_name, quantity_sold, total_price FROM sales JOIN inventory ON sales.item_id = inventory.item_id WHERE YEARWEEK(sale_date, 1) = YEARWEEK(CURDATE(), 1)"
        elif period == 'monthly':
            sql = "SELECT item_name, quantity_sold, total_price FROM sales JOIN inventory ON sales.item_id = inventory.item_id WHERE MONTH(sale_date) = MONTH(CURDATE())"
        else:
            print("Invalid period. Choose daily, weekly, or monthly.")
            return

        self.cursor.execute(sql)
        report = self.cursor.fetchall()
        print(f"--- {period.capitalize()} Sales Report ---")
        for row in report:
            print(f"{row[0]}: Sold {row[1]} @ ${row[2] / row[1]:.2f} each")
        print(f"Total Sales: ${sum(row[2] for row in report):.2f}")
