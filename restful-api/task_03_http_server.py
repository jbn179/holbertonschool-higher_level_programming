#!/usr/bin/python3
"""Simple HTTP server implementation using http.server module"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Handler for HTTP requests providing basic API endpoints"""
    
    def _send_json_response(self, data, status_code=200):
        """
        Send a JSON response with the specified status code
        
        Args:
            data: The data to be converted to JSON and sent
            status_code (int): HTTP status code (default: 200)
        """
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = json.dumps(data).encode('utf-8')
        self.wfile.write(response)

    def _send_text_response(self, text, status_code=200):
        """
        Send a plain text response with the specified status code
        
        Args:
            text (str): The text to be sent
            status_code (int): HTTP status code (default: 200)
        """
        self.send_response(status_code)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(text.encode('utf-8'))

    def do_GET(self):
        """
        Handle GET requests for different endpoints
        
        Endpoints:
            /: Returns a welcome message
            /data: Returns sample JSON data
            /status: Returns server status
            /info: Returns API information
            Others: Returns 404 error
        """
        if self.path == '/':
            # Root route - returns base message
            self._send_text_response("Hello, this is a simple API!")
        
        elif self.path == '/data':
            # /data route - returns JSON data
            sample_data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self._send_json_response(sample_data)
        
        elif self.path == '/status':
            # /status route - returns OK
            self._send_text_response("OK")

        elif self.path == '/info':
            # /info route - returns API information
            info_data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self._send_json_response(info_data)

        else:
            # Handle undefined endpoints
            error_data = {
                "error": "Endpoint not found",
                "path": self.path
            }
            self._send_json_response(error_data, 404)


def run_server(port=8000):
    """
    Start the HTTP server on the specified port
    
    Args:
        port (int): Port number to listen on (default: 8000)
    """
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print(f"Server running on port {port}...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down the server...")
        httpd.server_close()


if __name__ == "__main__":
    run_server()
