import bcrypt
import mysql.connector

class Auth:
    def __init__(self, db):
        self.db = db
        self.cursor = db.cursor()

    def register(self, username, password, role):
        # Hash the password using bcrypt
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        sql = "INSERT INTO users (username, password_hash, role) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, (username, password_hash, role))
        self.db.commit()
        print(f"User {username} registered successfully as {role}.")

    def login(self, username, password):
        # Query the database to check if the user exists
        sql = "SELECT password_hash, role FROM users WHERE username = %s"
        self.cursor.execute(sql, (username,))
        result = self.cursor.fetchone()

        if result:
            stored_password_hash, role = result
            """Check if the entered password matches the hashed password"""
            if bcrypt.checkpw(password.encode('utf-8'), stored_password_hash.encode('utf-8')):
                print(f"Login successful! Welcome, {username} ({role}).")
                return role
            else:
                print("Invalid password.")
                return None
        else:
            print("User not found.")
            return None
