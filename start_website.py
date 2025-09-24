#!/usr/bin/env python3
"""
Website Launcher for Save the Date
Starts a local web server to view the beautiful website
"""

import os
import sys
import webbrowser
import threading
import time
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

class SaveTheDateWebServer(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="website", **kwargs)
    
    def end_headers(self):
        # Add CORS headers to allow video access
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        super().end_headers()
    
    def log_message(self, format, *args):
        # Suppress default logging for cleaner output
        pass

def check_video_exists():
    """Check if the video file exists"""
    video_path = "output/save_the_date_simple.mp4"
    return os.path.exists(video_path)

def create_video_if_needed():
    """Create video if it doesn't exist"""
    if not check_video_exists():
        print("🎬 Video not found! Creating your Save-the-Date video...")
        print("⏳ This will take a few moments...")
        
        try:
            import subprocess
            result = subprocess.run([sys.executable, "create_simple_video.py"], 
                                  capture_output=True, text=True)
            
            if result.returncode == 0:
                print("✅ Video created successfully!")
                return True
            else:
                print("❌ Error creating video:")
                print(result.stderr)
                return False
        except Exception as e:
            print(f"❌ Error: {e}")
            return False
    return True

def open_browser(url, delay=2):
    """Open browser after a delay"""
    time.sleep(delay)
    try:
        webbrowser.open(url)
        print(f"🌐 Opening {url} in your default browser...")
    except Exception as e:
        print(f"❌ Could not open browser automatically: {e}")
        print(f"📱 Please manually open: {url}")

def start_server(port=8080):
    """Start the web server"""
    
    print("💍 Prathyusha & Sravan - Save the Date Website")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists("website"):
        print("❌ Website directory not found!")
        print("📁 Please run this script from the wedding project directory")
        return
    
    # Create video if needed
    if not create_video_if_needed():
        print("⚠️  Continuing without video - you can generate it later")
        print()
    
    # Start the server
    try:
        server_address = ('', port)
        httpd = HTTPServer(server_address, SaveTheDateWebServer)
        
        url = f"http://localhost:{port}"
        
        print(f"🚀 Starting website server...")
        print(f"🌐 Website URL: {url}")
        print(f"📱 Share this URL with family and friends!")
        print()
        print("✨ Website Features:")
        print("   • Beautiful responsive design")
        print("   • Video preview and download")
        print("   • Social media sharing guides")
        print("   • Wedding countdown timer")
        print("   • Mobile-friendly interface")
        print()
        print("🛑 Press Ctrl+C to stop the server")
        print("=" * 50)
        
        # Open browser in a separate thread
        browser_thread = threading.Thread(target=open_browser, args=(url,))
        browser_thread.daemon = True
        browser_thread.start()
        
        # Start the server
        httpd.serve_forever()
        
    except KeyboardInterrupt:
        print("\n👋 Shutting down website server...")
        httpd.shutdown()
        print("✅ Server stopped successfully!")
        
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"❌ Port {port} is already in use!")
            print(f"🔄 Trying port {port + 1}...")
            start_server(port + 1)
        else:
            print(f"❌ Server error: {e}")
    
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

def main():
    """Main function"""
    
    # Change to script directory
    script_dir = Path(__file__).parent.absolute()
    os.chdir(script_dir)
    
    # Check command line arguments
    port = 8080
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("❌ Invalid port number. Using default port 8080.")
    
    start_server(port)

if __name__ == "__main__":
    main()
