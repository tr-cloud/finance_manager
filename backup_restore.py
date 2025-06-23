import shutil

def backup_data():
    shutil.copyfile("finance.db", "backup_finance.db")
    print("✅ Backup complete.")

def restore_data():
    shutil.copyfile("backup_finance.db", "finance.db")
    print("✅ Data restored.")
