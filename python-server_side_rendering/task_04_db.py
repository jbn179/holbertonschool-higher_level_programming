from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def create_database():
    """Create and populate the SQLite database if it doesn't exist"""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    
    # Check if data already exists
    cursor.execute('SELECT COUNT(*) FROM Products')
    count = cursor.fetchone()[0]
    
    if count == 0:
        # Insert sample data
        cursor.execute('''
            INSERT INTO Products (id, name, category, price)
            VALUES
            (1, 'Laptop', 'Electronics', 799.99),
            (2, 'Coffee Mug', 'Home Goods', 15.99)
        ''')
    
    conn.commit()
    conn.close()

def read_json_data():
    """Read data from JSON file"""
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def read_csv_data():
    """Read data from CSV file"""
    products = []
    try:
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert id to int and price to float
                try:
                    row['id'] = int(row['id'])
                    row['price'] = float(row['price'])
                    products.append(row)
                except (ValueError, KeyError):
                    # Skip rows with invalid data
                    continue
        return products
    except FileNotFoundError:
        return []

def read_sqlite_data(product_id=None):
    """Read data from SQLite database"""
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row  # This enables column access by name
        cursor = conn.cursor()
        
        if product_id is not None:
            cursor.execute('SELECT * FROM Products WHERE id = ?', (product_id,))
        else:
            cursor.execute('SELECT * FROM Products')
            
        rows = cursor.fetchall()
        conn.close()
        
        # Convert to list of dictionaries
        products = []
        for row in rows:
            products.append({
                'id': row['id'],
                'name': row['name'],
                'category': row['category'],
                'price': row['price']
            })
        
        return products
    except sqlite3.Error:
        return []

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    # Initialize variables
    products_data = []
    error_message = None
    
    # Convert product_id to integer if provided
    if product_id:
        try:
            product_id = int(product_id)
        except ValueError:
            error_message = "Invalid ID format"
            product_id = None
    
    # Get data based on source
    if error_message is None:
        if source == 'json':
            products_data = read_json_data()
            # Filter by ID if provided
            if product_id:
                products_data = [p for p in products_data if p.get('id') == product_id]
                if not products_data:
                    error_message = "Product not found"
        elif source == 'csv':
            products_data = read_csv_data()
            # Filter by ID if provided
            if product_id:
                products_data = [p for p in products_data if p.get('id') == product_id]
                if not products_data:
                    error_message = "Product not found"
        elif source == 'sql':
            # For SQL, we filter at the database level
            products_data = read_sqlite_data(product_id)
            if product_id and not products_data:
                error_message = "Product not found"
        else:
            error_message = "Wrong source"
    
    return render_template('product_display.html', 
                           products=products_data, 
                           error=error_message)

if __name__ == '__main__':
    # Create database when the application starts
    create_database()
    app.run(debug=True, port=5000)