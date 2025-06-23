import bcrypt
import getpass
from db.database import connect_db

def register_user():
    conn = connect_db()
    cursor = conn.cursor()
    username = input("Choose a username: ")
    password = getpass.getpass("Choose a password: ")
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed))
        conn.commit()
        print("✅ Registration successful!")
    except:
        print("❌ Username already exists.")
    conn.close()

def login_user():
    conn = connect_db()
    cursor = conn.cursor()
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    cursor.execute("SELECT id, password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    if result and bcrypt.checkpw(password.encode(), result[1]):
        print("✅ Login successful!")
        return result[0]
    else:
        print("❌ Invalid credentials.")
        return None
