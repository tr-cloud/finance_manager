from db.database import initialize_db
from auth.auth import register_user, login_user
from finance.transactions import add_transaction, view_transactions, delete_transaction
from finance.reports import generate_monthly_report
from finance.budgeting import set_budget
from backup.backup_restore import backup_data, restore_data

def main():
    initialize_db()
    user_id = None

    while True:
        print("\n🔐 1. Register  2. Login  3. Exit")
        choice = input("Choose: ")
        if choice == '1':
            register_user()
        elif choice == '2':
            user_id = login_user()
            if user_id:
                break
        elif choice == '3':
            return
        else:
            print("❌ Invalid input.")

    while True:
        print("\n📋 MENU")
        print("1. Add Transaction\n2. View Transactions\n3. Delete Transaction")
        print("4. Monthly Report\n5. Set Budget\n6. Backup\n7. Restore\n8. Exit")
        ch = input("Choose: ")

        if ch == '1':
            add_transaction(user_id)
        elif ch == '2':
            view_transactions(user_id)
        elif ch == '3':
            delete_transaction(user_id)
        elif ch == '4':
            generate_monthly_report(user_id)
        elif ch == '5':
            set_budget(user_id)
        elif ch == '6':
            backup_data()
        elif ch == '7':
            restore_data()
        elif ch == '8':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
