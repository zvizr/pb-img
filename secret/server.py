import os
from http.server import BaseHTTPRequestHandler, HTTPServer

try:
    with open("/secret.sha256") as f:
        SHA = f.read().strip()
except OSError:
    SHA = "none"


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = f"PB-IMG {os.getuid()}\nsha={SHA}\n".encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass


HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
