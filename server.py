#!/usr/bin/env python3
"""
Simple Python HTTP server to serve static HTML files for Byte Blog
Serves files from current directory on 0.0.0.0:5000 as required by Replit
"""

import http.server
import socketserver
import os

# Configuration for Replit
HOST = "0.0.0.0"  # Required by Replit for external access
PORT = 5000       # Required by Replit

# Set the directory to serve (current directory where HTML files are)
web_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(web_dir)

# Create HTTP request handler
Handler = http.server.SimpleHTTPRequestHandler

print(f"Starting Byte Blog server on {HOST}:{PORT}")
print(f"Serving directory: {web_dir}")
print("Available at: http://0.0.0.0:5000")

# Start the server
with socketserver.TCPServer((HOST, PORT), Handler) as httpd:
    print("Server running... Press Ctrl+C to stop")
    httpd.serve_forever()