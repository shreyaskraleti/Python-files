import mysql.connector
from datetime import datetime, timedelta

class Reports:
    def __init__(self, db):
        self.db = db
        self.cursor = db.cursor()

    def generate_report(self, period):
        try:
            if period not in ['daily', 'weekly', 'monthly']:
                print("Invalid period. Please choose 'daily', 'weekly', or 'monthly'.")
                return

            # Define the date range based on the selected period
            end_date = datetime.now()
            if period == 'daily':
                start_date = end_date - timedelta(days=1)
            elif period == 'weekly':
                start_date = end_date - timedelta(weeks=1)
            elif period == 'monthly':
                start_date = end_date - timedelta(days=30)

            # Format dates for SQL query
            start_date_str = start_date.strftime('%Y-%m-%d')
            end_date_str = end_date.strftime('%Y-%m-%d')

            print(f"Generating {period} report...")  # Indicating report generation
            print(f"Start Date: {start_date_str}, End Date: {end_date_str}")  # Debugging

            # SQL query to fetch sales data within the date range
            sql = """
                SELECT item_name, SUM(quantity_sold) AS total_sold
                FROM sales
                WHERE sale_date BETWEEN %s AND %s
                GROUP BY item_name
            """

            print("Executing SQL query...")  # Debugging
            self.cursor.execute(sql, (start_date_str, end_date_str))
            print("SQL query executed.")  # Debugging
            
            results = self.cursor.fetchall()
            print(f"Results fetched: {results}")  # Debugging

            # Display report
            if results:
                print(f"\n{period.capitalize()} Sales Report:")
                print(f"From {start_date_str} to {end_date_str}")
                print("-" * 30)
                for row in results:
                    item_name, total_sold = row
                    print(f"Item: {item_name}, Quantity Sold: {total_sold}")
            else:
                print("No sales data found for this period.")

        except mysql.connector.Error as err:
            print(f"Error generating report: {err}")
