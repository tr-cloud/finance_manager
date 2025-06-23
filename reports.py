from db.database import connect_db

def generate_monthly_report(user_id):
    month = input("Enter month (YYYY-MM): ")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT type, SUM(amount) FROM transactions
        WHERE user_id = ? AND date LIKE ?
        GROUP BY type
    """, (user_id, f"{month}%"))
    rows = cursor.fetchall()
    income, expense = 0, 0
    for t_type, total in rows:
        if t_type == 'income':
            income = total
        else:
            expense = total
    savings = income - expense
    print(f"\n📆 {month} Report:")
    print(f"Total Income: ₹{income}")
    print(f"Total Expense: ₹{expense}")
    print(f"Net Savings: ₹{savings}")
    conn.close()
