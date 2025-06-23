from db.database import connect_db

def set_budget(user_id):
    category = input("Enter category: ")
    month = input("Enter month (YYYY-MM): ")
    limit = float(input("Enter limit amount: "))

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO budgets (user_id, category, month, limit_amount)
        VALUES (?, ?, ?, ?)
    """, (user_id, category, month, limit))
    conn.commit()
    conn.close()
    print("✅ Budget set!")

def check_budget(user_id, category, amount, month):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT limit_amount FROM budgets
        WHERE user_id = ? AND category = ? AND month = ?
    """, (user_id, category, month))
    result = cursor.fetchone()
    if result and amount > result[0]:
        print("⚠️ Budget limit exceeded!")
    conn.close()
