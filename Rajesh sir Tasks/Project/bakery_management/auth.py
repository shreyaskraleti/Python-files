import bcrypt
import mysql.connector

class Auth:
    def __init__(self, db):
        self.db = db
        self.cursor = db.cursor()
        
    def register(self, username, password, role):
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        sql = "INSERT INTO users (username, password_hash, role) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, (username, password_hash, role))
        self.db.commit()
        print(f"User {username} registered successfully as {role}.")
    
    def login(self, username, password):
        sql = "SELECT password_hash, role FROM users WHERE username = %s"
        self.cursor.execute(sql, (username,))
        result = self.cursor.fetchone()
        if result and bcrypt.checkpw(password.encode('utf-8'), result[0].encode('utf-8')):
            print(f"Login successful! Welcome, {username} ({result[1]}).")
            return result[1]
        else:
            print("Invalid username or password.")
            return None