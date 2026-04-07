from http.server import BaseHTTPRequestHandler, HTTPServer
import time, os

SAVE_DIR = "captures"
os.makedirs(SAVE_DIR, exist_ok=True)

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        data = self.rfile.read(length)
        filename = f"{SAVE_DIR}/img_{int(time.time()*1000)}.jpg"
        with open(filename, "wb") as f:
            f.write(data)
        print(f"Saved {filename}  ({len(data)} bytes)")
        self.send_response(200)
        self.end_headers()

    def log_message(self, *args):
        pass  # suppress default HTTP logs

print("Listening on port 8080...")
HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()