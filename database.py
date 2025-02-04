import sqlite3
import os

db_name = 'expenses.db'

def connect():
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    return conn, cursor

def create_db():
    conn, cursor = connect()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS expenses(
                   id INTEGER PRIMARY KEY AUTOINCREMENT, 
                   amount REAL NOT NULL, 
                   category TEXT NOT NULL, 
                   date TEXT NOT NULL, 
                   description TEXT, 
                   payment_method TEXT NOT NULL, 
                   merchant TEXT NOT NULL, 
                   recurring INTEGER DEFAULT 0, 
                   created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
                   ''')    
    conn.commit()
    conn.close()

def add_expense(amount, category, date, description, payment_method, merchant, recurring=0):
    conn, cursor = connect()
    cursor.execute('''
                   INSERT INTO expenses (amount, category, date, description, payment_method, merchant, recurring)
                   VALUES (?, ?, ?, ?, ?, ?, ?)
                   ''', (amount, category, date, description, payment_method, merchant, recurring))
    conn.commit()
     
    # Retrieve all expenses immediately after insertion
    cursor.execute("SELECT * FROM expenses")
    print("All Expenses After Insertion:", cursor.fetchall())  # This should show the newly added expense
    
    conn.close()

def get_expenses():
    conn, cursor = connect()
    cursor.execute("SELECT * FROM expenses ORDER BY date DESC")
    expenses = cursor.fetchall()
    conn.close()
    return expenses

def update_expense(id, amount, category, date, description, payment_method, merchant, recurring):
    conn, cursor = connect()
    update_fields = []
    values = []
    
    if amount is not None:
        update_fields.append("amount = ?")
        values.append(amount)
        
    if category is not None:
        update_fields.append("category = ?")
        values.append(category)
    
    if date is not None:
        update_fields.append("date = ?")
        values.append(date)
    
    if description is not None:
        update_fields.append("description = ?")
        values.append(description)
    
    if payment_method is not None:
        update_fields.append("payment_method = ?")
        values.append(payment_method)
        
    if merchant is not None:
        update_fields.append("merchant = ?")
        values.append(merchant)
        
    if recurring is not None:
        update_fields.append("recurring = ?")
        values.append(recurring)
    
def delete_expense(id):
    conn, cursor = connect()
    cursor.execute("DELETE FROM expenses where id = ?", (id,))
    conn.commit()
    conn.close()
    
def drop_db():
    conn, cursor = connect()
    cursor.execute("DROP TABLE IF EXISTS expenses")
    conn.commit()
    conn.close()