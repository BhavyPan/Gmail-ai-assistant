from http.server import BaseHTTPRequestHandler
import json
import os
import sys

# Add the parent directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # Import and run Flask app
            from app import app
            # This is a simplified handler - in practice, you'd want WSGI integration
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Gmail AI Assistant API is running')
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(f'Error: {str(e)}'.encode())
    
    def do_POST(self):
        self.do_GET()

# Vercel serverless function handler
def main(request, response):
    try:
        from app import app
        # This would need proper WSGI adapter for full functionality
        return response.json({"status": "running", "message": "Gmail AI Assistant"})
    except Exception as e:
        return response.json({"error": str(e)}, status=500)
