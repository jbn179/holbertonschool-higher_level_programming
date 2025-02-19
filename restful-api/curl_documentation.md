# 🚀 The Ultimate CURL Command Guide - Master HTTP Requests Like a Pro! 🛠️

## Overview 📋
cURL (Client URL) is a command-line tool and library for transferring data using various protocols. It's widely used for testing, debugging, and making HTTP requests.

## Basic Syntax ⌨️
```bash
curl [options] <url>
```

## Key Commands and Options 🎯

### HTTP Methods 📡
- **GET request** (default):
```bash
curl http://example.com
```

- **POST request**:
```bash
curl -X POST http://example.com
```

- **PUT request**:
```bash
curl -X PUT http://example.com
```

- **DELETE request**:
```bash
curl -X DELETE http://example.com
```

### Common Options ⚙️
| Option | Description |
|--------|-------------|
| `-o <file>` | Save output to file |
| `-i` | Include response headers |
| `-I` | Fetch headers only |
| `-v` | Verbose mode |
| `-s` | Silent mode |

### Working with Headers 📋
```bash
# Add custom header
curl -H "Content-Type: application/json" http://example.com

# Include response headers
curl -i http://example.com
```

### Data Transmission 📤
```bash
# Send POST data
curl -d "name=john&age=25" http://example.com

# Send JSON data
curl -X POST -H "Content-Type: application/json" \
     -d '{"name":"john","age":25}' http://example.com
```

### Authentication 🔐
```bash
# Basic authentication
curl -u username:password http://example.com

# Bearer token
curl -H "Authorization: Bearer <token>" http://example.com
```

### SSL/TLS Options 🔒
- `-k`: Allow insecure connections
- `--cacert`: Specify certificate
- `--cert`: Client certificate

### Download Features ⬇️
```bash
# Download file
curl -O http://example.com/file.zip

# Resume download
curl -C - -O http://example.com/file.zip
```

### Advanced Features 🔧

#### Follow Redirects
```bash
curl -L http://example.com
```

#### Progress Meter
```bash
curl -# http://example.com/large-file.zip
```

#### Multiple URLs
```bash
curl http://site1.com http://site2.com
```

## Common Use Cases 💡

### API Testing 🔍
```bash
# GET request with authentication and JSON response
curl -H "Authorization: Bearer token123" \
     -H "Accept: application/json" \
     https://api.example.com/users
```

### File Upload 📁
```bash
# Upload single file
curl -F "file=@localfile.jpg" http://example.com/upload

# Upload multiple files
curl -F "file1=@file1.jpg" -F "file2=@file2.jpg" http://example.com/upload
```

### Cookie Handling 🍪
```bash
# Save cookies
curl -c cookies.txt http://example.com

# Use saved cookies
curl -b cookies.txt http://example.com
```

## Troubleshooting Tips ⚠️
- Use `-v` for detailed debugging
- Use `-I` to check headers only
- Use `-k` for self-signed certificates
- Use `-L` if getting redirect errors

## Best Practices ✨
1. Always quote URLs containing special characters
2. Use appropriate Content-Type headers
3. Consider using `-f` to fail silently
4. Use `-s` in scripts to suppress progress meter
5. Always validate SSL certificates unless testing

## Error Codes ❌
Common curl exit codes:
- `0`: Success
- `6`: Could not resolve host
- `7`: Failed to connect
- `22`: HTTP page not retrieved
- `35`: SSL connect error

## Author
<li> Benjamin RISTORD - <a href="https://github.com/jbn179">@jbn179</a></li>
