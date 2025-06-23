from db.database import connect_db
from datetime import datetime

def add_transaction(user_id):
    t_type = input("Type (income/expense): ").lower()
    category = input("Category: ")
    amount = float(input("Amount: "))
    note = input("Note: ")
    date = datetime.now().strftime("%Y-%m-%d")

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO transactions (user_id, type, category, amount, date, note)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (user_id, t_type, category, amount, date, note))
    conn.commit()
    conn.close()
    print("✅ Transaction added!")

def view_transactions(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions WHERE user_id = ?", (user_id,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()

def delete_transaction(user_id):
    view_transactions(user_id)
    tid = int(input("Enter transaction ID to delete: "))
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM transactions WHERE id = ? AND user_id = ?", (tid, user_id))
    conn.commit()
    conn.close()
    print("✅ Transaction deleted.")
