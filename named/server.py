import os
from http.server import BaseHTTPRequestHandler, HTTPServer

DATA = "ok"
try:
    with open("/data/probe", "w") as f:
        f.write(str(os.getuid()))
except OSError:
    DATA = "fail"


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = f"PB-IMG {os.getuid()}\ndata={DATA}\n".encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass


HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
