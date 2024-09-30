import bcrypt
import mysql.connector

class Auth:
    def __init__(self, db):
        self.db = db
        self.cursor = db.cursor()

    def register(self, username, password, role):
        try:
            # Hash the password and decode to store it as a string
            password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            sql = "INSERT INTO users (username, password_hash, role) VALUES (%s, %s, %s)"
            self.cursor.execute(sql, (username, password_hash, role))
            self.db.commit()
            print(f"User {username} registered successfully as {role}.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
    
    def login(self, username, password):
        try:
            sql = "SELECT password_hash, role FROM users WHERE username = %s"
            self.cursor.execute(sql, (username,))
            result = self.cursor.fetchone()

            if result:
                print(f"User {username} found.")
                stored_password_hash = result[0]

                if bcrypt.checkpw(password.encode('utf-8'), stored_password_hash.encode('utf-8')):
                    print(f"Login successful! Welcome, {username} ({result[1]}).")
                    return result[1]
                else:
                    print("Incorrect password.")
                    return None
            else:
                print(f"User {username} not found.")
                return None
        except mysql.connector.Error as err:
            print(f"Error during login: {err}")
            return None
