# 🌐 HTTP vs HTTPS: Complete Protocol Guide
## A Comprehensive Guide to Web Communication Protocols

## Differences between HTTP and HTTPS

### Security
- **HTTP** (Hypertext Transfer Protocol)
  - Does not encrypt data
  - Vulnerable to eavesdropping
- **HTTPS** (Hypertext Transfer Protocol Secure)
  - Adds SSL/TLS encryption layer
  - Protects data exchange between clients and servers
  - Prevents interception and tampering

### Usage
- **HTTPS**: Used for sensitive information (banking, e-commerce)
- **HTTP**: Used for non-sensitive content

***Note***:  The "s" in HTTPS stands for "secure"

## HTTP Communication Structure

### HTTP Request Structure
| Component | Description | Example |
|-----------|-------------|---------|
| Method | Action to be performed | GET, POST, PUT, DELETE |
| URL | Resource being requested | `/api/users` |
| Headers | Additional information | User-Agent, Accept, Content-Type |
| Body | Optional data payload | Form data, JSON content |

### HTTP Response Structure
| Component | Description | Example |
|-----------|-------------|---------|
| Status Code | Result indicator | 200, 404, 500 |
| Status Message | Brief description | OK, Not Found |
| Headers | Response metadata | Content-Type, Content-Length |
| Body | Requested content | HTML, JSON data |

## Common HTTP Methods

### GET
- 📥 **Description**: Retrieves data from the server
- 💡 **Use Cases**: 
  1. Fetching a web page or API data
  2. Retrieving user profile information

### POST
- 📤 **Description**: Sends data to the server
- 💡 **Use Cases**:
  1. Submitting forms or uploading files
  2. Creating a new resource (user account, blog post)

### PUT
- 🔄 **Description**: Updates existing server data
- 💡 **Use Cases**:
  1. Modifying profile information
  2. Updating an entire resource's content

### DELETE
- 🗑️ **Description**: Removes server data
- 💡 **Use Cases**:
  1. Deleting user accounts
  2. Removing posts or comments from a blog

## HTTP Status Codes

### 1xx - Informational Responses
- **100 Continue**
  - 📡 *Description*: Server received request headers, client should proceed with request
  - *Example*: Large file upload confirmation
- **101 Switching Protocols**
  - 🔄 *Description*: Server agrees to switch protocols
  - *Example*: Upgrading from HTTP to WebSocket

### 2xx - Success Responses
- **200 OK**
  - ✅ *Description*: Request succeeded
  - *Example*: Successfully loading a webpage
- **201 Created**
  - 📝 *Description*: Request succeeded and new resource created
  - *Example*: Successfully creating a new user account

### 3xx - Redirection
- **301 Moved Permanently**
  - 🔄 *Description*: Resource permanently moved to new URL
  - *Example*: Website domain change
- **302 Found**
  - 🔀 *Description*: Resource temporarily moved
  - *Example*: Temporary redirect during maintenance

### 4xx - Client Errors
- **404 Not Found**
  - ❌ *Description*: Resource not found on server
  - *Example*: Accessing non-existent page
- **403 Forbidden**
  - 🚫 *Description*: Access to resource forbidden
  - *Example*: Attempting to access restricted content

### 5xx - Server Errors
- **500 Internal Server Error**
  - 💥 *Description*: Generic server error
  - *Example*: Unhandled exception in server code
- **503 Service Unavailable**
  - 🔧 *Description*: Server temporarily unable to handle request
  - *Example*: Server under maintenance or overloaded

## Authors
<li> Benjamin RISTORD - <a href="https://github.com/jbn179">@jbn179</a></li>