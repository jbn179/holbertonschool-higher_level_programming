#!/usr/bin/python3
"""Simple HTTP server implementation using http.server module"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Handler for the HTTP requests"""
    
    def _send_json_response(self, data, status_code=200):
        """Helper method to send JSON responses"""
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = json.dumps(data).encode('utf-8')
        self.wfile.write(response)

    def _send_text_response(self, text, status_code=200):
        """Helper method to send text responses"""
        self.send_response(status_code)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(text.encode('utf-8'))

    def do_GET(self):
        """Handle GET requests"""
        if self.path == '/':
            # Route racine - renvoie le message de base
            self._send_text_response("Hello, this is a simple API!")
        
        elif self.path == '/data':
            # Route /data - renvoie les données JSON
            sample_data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self._send_json_response(sample_data)
        
        elif self.path == '/status':
            # Route /status - renvoie "OK"
            self._send_text_response("OK")

        elif self.path == '/info':
            # Route /info - renvoie les informations sur l'API
            info_data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self._send_json_response(info_data)

        else:
            # Gestion des endpoints non définis
            error_data = {
                "error": "Endpoint not found",
                "path": self.path
            }
            self._send_json_response(error_data, 404)


def run_server(port=8000):
    """Start the HTTP server"""
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
