from flask import Blueprint, render_template, request, jsonify
from database import add_expense, get_expenses, update_expense, delete_expense
from datetime import datetime

main = Blueprint('main', __name__)

# Render Home Page
@main.route("/")
def home():
    return render_template("home.html")

# Add Expense Route
@main.route("/add_expense", methods=["POST"])
def add_expense_route():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No Data Provided"}), 400 # Handle Missing Data
    
    try:
        # Extracting Fields
        amount = float(data.get("amount"))
        category = data.get("category")
        date = data.get("date")
        description = data.get("description")
        payment_method = data.get("payment_method")
        merchant = data.get("merchant")
        recurring = int(data.get("recurring", 0))
        
        # Ensure Amount Is Positive
        if amount <= 0:
            return jsonify({"error": "Amount must be greater than 0"}), 400
        
        # Validate Date Format
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400
    
    except ValueError:
        return jsonify({"error": "Invalid data type for amount or recurring"}), 400
    
    # Basic Validation
    if not all([amount, category, date, description, payment_method, merchant]):
        return jsonify({"error": "Missing Required Fields"}), 400    
    
    # Call Database Function
    add_expense(amount, category, date, description, payment_method, merchant, recurring)
    
    return jsonify({"message": "Expense Added Successfully"}), 201

# Get Expenses Route
@main.route("/get_expenses", methods=["GET"])
def get_expenses_route():
    
    # Fetch Expenses
    expenses = get_expenses()
    
    # Error Handling
    if not expenses:
        return jsonify({"error": "No Expenses Found"}), 404
    
    # Return the expenses data as a JSON response
    return jsonify(expenses), 200

# Update Expense Route
@main.route("/update_expense/<int:id>", methods=["PUT"])
def update_expense_route(id):
    data = request.get_json()
    
    # Error Hnadling
    if not data:
        return jsonify({"error": "No Data Provided"}), 400
    
    try:
        # Extracting Fields
        amount = float(data.get("amount"))
        category = data.get("category")
        date = data.get("date")
        description = data.get("description")
        payment_method = data.get("payment_method")
        merchant = data.get("merchant")
        recurring = int(data.get("recurring", 0))
    
        # Error Handling
        if amount <= 0:
            return jsonify({"error": "Amount must be greater than 0"}), 400
        
        # Validate Date Format
            try:
                datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400
        
    except ValueError:
        return jsonify({"error": "Invalid data type for amount or recurring"}), 400
    
    # Basic Validation
    if not all([amount, category, date, description, payment_method, merchant]):
        return jsonify({"error": "Missing Required Fields"}), 400
    
    expense = get_expense_by_id(id)
    
    if not expense:
        return jsonify({"error": "Expense Not Found"}), 404
    
    update_expense(id, amount, category, date, description, payment_method, merchant, recurring)
    
    return jsonify({"message": "Expense Updated Successfully"}), 200