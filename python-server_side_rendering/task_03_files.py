from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

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

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    # Initialize variables
    products_data = []
    error_message = None
    
    # Get data based on source
    if source == 'json':
        products_data = read_json_data()
    elif source == 'csv':
        products_data = read_csv_data()
    else:
        error_message = "Wrong source"
        
    # Filter by ID if provided
    if product_id and not error_message:
        try:
            product_id = int(product_id)
            filtered_products = [p for p in products_data if p.get('id') == product_id]
            if filtered_products:
                products_data = filtered_products
            else:
                error_message = "Product not found"
        except ValueError:
            error_message = "Invalid ID format"
    
    return render_template('product_display.html', 
                           products=products_data, 
                           error=error_message)

if __name__ == '__main__':
    app.run(debug=True, port=5000)