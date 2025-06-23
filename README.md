# Personal Finance Manager — CLI Python App

A command-line application to help users track income, expenses, budgets, and savings. Built in Python using SQLite for data storage and bcrypt for secure authentication.

This application includes user registration and login (with secure password hashing using bcrypt), income and expense tracking, category-based budget setting, financial reporting, and backup/restore features.

To install and run the application:

1. Clone the Repository

git clone https://github.com/tr-cloud/finance-manager-cli  
cd finance-manager-cli

2. (Optional) Create a Virtual Environment

python -m venv venv

Activate it:  
On Windows:  
venv\Scripts\activate  
On macOS/Linux:  
source venv/bin/activate

3. Install Required Dependencies

pip install bcrypt

If you have a requirements.txt file, you can also run:

pip install -r requirements.txt

4. Run the Application

python main.py

Once the app starts, you can register a user account, log in, and use the interactive menu to add/view/delete transactions, generate monthly reports, set category-based budgets, and back up or restore your data.

Requirements:
- Python 3.8 or higher
- bcrypt
- sqlite3 (built-in with Python)

To back up your data, the app will create a backup_finance.db file. You can restore it later to recover your saved transactions and budgets.

This project is licensed under the MIT License.

Contributions are welcome. Fork the repository and submit a pull request if you'd like to improve the app.
