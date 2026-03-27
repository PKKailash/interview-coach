#!/usr/bin/env python3
"""
Interview Coach - Local Server Launcher
Serves the interview prep app at http://localhost:8765
"""
import http.server
import socketserver
import webbrowser
import os
import sys
import threading

PORT = 8765
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=SCRIPT_DIR, **kwargs)
    def log_message(self, format, *args):
        pass  # suppress request logs

def open_browser():
    import time
    time.sleep(0.8)
    webbrowser.open(f"http://localhost:{PORT}/interview_app.html")

if __name__ == "__main__":
    print(f"\n🎙  Interview Coach is starting…")
    print(f"📍  Serving from: {SCRIPT_DIR}")
    print(f"🌐  Opening at:   http://localhost:{PORT}/interview_app.html")
    print(f"\nPress Ctrl+C to stop the server.\n")

    threading.Thread(target=open_browser, daemon=True).start()

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n✅  Server stopped.")
            sys.exit(0)
