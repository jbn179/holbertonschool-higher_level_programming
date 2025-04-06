# RESTful API 🌐

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-green.svg)
![REST](https://img.shields.io/badge/REST-API-orange.svg)

## 📖 Description
This project implements a RESTful API using Python and Flask. It demonstrates the principles of Representational State Transfer (REST) architecture for creating scalable web services. The API provides endpoints for CRUD operations (Create, Read, Update, Delete) on resources, handles authentication and authorization, and formats responses according to REST best practices.

## 📂 Contents
- **task_02_requests.py**: Script demonstrating how to make HTTP requests in Python
- **task_03_http_server.py**: Implementation of a basic HTTP server
- **task_04_flask.py**: Simple RESTful API using Flask
- **task_05_basic_security.py**: API implementation with basic security features
- **main_02_requests.py**: Test script for HTTP requests
- **curl_documentation.md**: Documentation for testing APIs with curl
- **http_documentation.md**: Documentation about HTTP protocol
- **posts.csv**: Sample data used by the API
- **requirements.txt**: Python dependencies for the project

## 🚀 Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/username/holbertonschool-higher_level_programming.git
   ```

2. Navigate to the project directory:
   ```bash
   cd holbertonschool-higher_level_programming/restful-api
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   export FLASK_APP=app.py
   export FLASK_ENV=development
   ```

5. Run the Flask development server:
   ```bash
   flask run
   ```

6. Access the API at:
   ```
   http://localhost:5000/api/v1/
   ```

## 🛠️ Requirements
- Python 3.8+
- Flask 2.0+
- Flask-RESTful
- Flask-SQLAlchemy
- Flask-JWT-Extended
- Postman or curl (for testing)

## API Endpoints ✨

### Authentication
- **POST /api/v1/auth/register**: Register a new user
- **POST /api/v1/auth/login**: Authenticate and receive a JWT token
- **POST /api/v1/auth/refresh**: Refresh an authentication token
- **POST /api/v1/auth/logout**: Invalidate a token

### Users
- **GET /api/v1/users**: Get all users (admin only)
- **GET /api/v1/users/{id}**: Get a specific user
- **PUT /api/v1/users/{id}**: Update a user
- **DELETE /api/v1/users/{id}**: Delete a user

### Items
- **GET /api/v1/items**: Get all items
- **GET /api/v1/items/{id}**: Get a specific item
- **POST /api/v1/items**: Create a new item
- **PUT /api/v1/items/{id}**: Update an item
- **DELETE /api/v1/items/{id}**: Delete an item

## Key Concepts ✨
- **REST Architecture**: Designing stateless, resource-oriented APIs
- **HTTP Methods**: Using GET, POST, PUT, DELETE appropriately
- **Status Codes**: Returning appropriate HTTP status codes
- **Authentication**: Implementing JWT-based authentication
- **Serialization**: Converting between Python objects and JSON
- **Input Validation**: Validating and sanitizing inputs
- **HATEOAS**: Hypermedia as the Engine of Application State

## Examples

### API Resource Implementation
```python
from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.item import ItemModel
from schemas.item import ItemSchema

item_schema = ItemSchema()
item_list_schema = ItemSchema(many=True)

class Item(Resource):
    @jwt_required()
    def get(self, item_id):
        """Get a specific item by ID"""
        item = ItemModel.find_by_id(item_id)
        if item:
            return item_schema.dump(item), 200
        return {"message": "Item not found"}, 404

    @jwt_required()
    def put(self, item_id):
        """Update an existing item"""
        item_data = request.get_json()
        item = ItemModel.find_by_id(item_id)
        
        if not item:
            return {"message": "Item not found"}, 404
            
        # Update item attributes
        item.name = item_data.get("name", item.name)
        item.price = item_data.get("price", item.price)
        item.save_to_db()
        
        return item_schema.dump(item), 200

    @jwt_required()
    def delete(self, item_id):
        """Delete an item"""
        item = ItemModel.find_by_id(item_id)
        if not item:
            return {"message": "Item not found"}, 404
            
        item.delete_from_db()
        return {"message": "Item deleted"}, 200


class ItemList(Resource):
    def get(self):
        """Get all items"""
        items = ItemModel.find_all()
        return item_list_schema.dump(items), 200
        
    @jwt_required()
    def post(self):
        """Create a new item"""
        item_data = request.get_json()
        item = item_schema.load(item_data)
        
        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500
            
        return item_schema.dump(item), 201
```

### Testing with curl
```bash
# Register a new user
curl -X POST -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "password123"}' \
  http://localhost:5000/api/v1/auth/register

# Login and get token
curl -X POST -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "password123"}' \
  http://localhost:5000/api/v1/auth/login

# Get all items (with token)
curl -X GET -H "Content-Type: application/json" \
  -H "Authorization: Bearer <your_token>" \
  http://localhost:5000/api/v1/items

# Create a new item
curl -X POST -H "Content-Type: application/json" \
  -H "Authorization: Bearer <your_token>" \
  -d '{"name": "Test Item", "price": 19.99}' \
  http://localhost:5000/api/v1/items
```

## Best Practices 🔍
- Use appropriate HTTP methods for operations (GET, POST, PUT, DELETE)
- Return proper status codes (200 OK, 201 Created, 400 Bad Request, 404 Not Found, etc.)
- Implement authentication and authorization mechanisms
- Validate all input data to prevent security vulnerabilities
- Use descriptive error messages to facilitate debugging
- Version your API (e.g., v1, v2) to maintain backward compatibility
- Implement pagination for large collections of resources
- Follow HATEOAS principles by including relevant links in responses
- Use consistent data formats (typically JSON)
- Document your API thoroughly with examples

## Resources 📚
- [REST API Concepts and Examples](https://restfulapi.net/)
- [Understanding REST Parameters](https://www.restapitutorial.com/lessons/restfulresourcenaming.html)
- [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Flask-RESTful Documentation](https://flask-restful.readthedocs.io/)
- [JSON Web Tokens](https://jwt.io/)

## License
![License](https://img.shields.io/badge/License-MIT-green.svg)  
This project is licensed under the MIT License - see the LICENSE file for details.

## Author ✍️
- Benjamin Nougué-Ristord