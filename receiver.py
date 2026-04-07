from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import time, os

SAVE_DIR = "captures"
os.makedirs(SAVE_DIR, exist_ok=True)

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Parse ?type=normal or ?type=ir from URL
        params = parse_qs(urlparse(self.path).query)
        img_type = params.get("type", ["unknown"])[0]

        length = int(self.headers.get("Content-Length", 0))
        data = self.rfile.read(length)

        timestamp = int(time.time() * 1000)
        filename = f"{SAVE_DIR}/{timestamp}_{img_type}.jpg"

        with open(filename, "wb") as f:
            f.write(data)

        print(f"Saved {filename}  ({len(data)} bytes)")

        self.send_response(200)
        self.end_headers()

    def log_message(self, *args):
        pass

print("Listening on port 8080...")
HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
