#!/usr/bin/env python3
"""
Save the Date - Simple Web App
A web-based interface for downloading and sharing the video
"""

import os
import shutil
from pathlib import Path
from http.server import HTTPServer, SimpleHTTPRequestHandler
import urllib.parse
import json
import webbrowser
import threading
import time

class SaveTheDateWebHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(self.get_main_page().encode())
        elif self.path == '/download':
            self.download_video()
        elif self.path == '/info':
            self.send_video_info()
        elif self.path.startswith('/video'):
            self.serve_video()
        else:
            super().do_GET()
    
    def get_main_page(self):
        """Generate the main HTML page"""
        video_exists = os.path.exists("output/save_the_date_simple.mp4")
        video_size = ""
        
        if video_exists:
            size_bytes = os.path.getsize("output/save_the_date_simple.mp4")
            size_mb = size_bytes / (1024 * 1024)
            video_size = f"{size_mb:.1f} MB"
        
        return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>💍 Save the Date - Prathyusha & Sravan</title>
    <style>
        body {{
            font-family: Georgia, serif;
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            color: #333;
        }}
        
        .container {{
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }}
        
        .header {{
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            padding: 30px;
            text-align: center;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }}
        
        .header h1 {{
            color: #2c3e50;
            margin: 0 0 10px 0;
            font-size: 2.5em;
        }}
        
        .header p {{
            color: #7f8c8d;
            font-size: 1.2em;
            margin: 0;
        }}
        
        .card {{
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            padding: 25px;
            margin-bottom: 20px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }}
        
        .video-info {{
            background: #f8f9fa;
            padding: 15px;
            border-radius: 10px;
            border-left: 5px solid #3498db;
            margin-bottom: 20px;
        }}
        
        .btn {{
            display: inline-block;
            padding: 12px 25px;
            margin: 10px;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            font-weight: bold;
            text-decoration: none;
            cursor: pointer;
            transition: all 0.3s;
        }}
        
        .btn-primary {{
            background: #3498db;
            color: white;
        }}
        
        .btn-primary:hover {{
            background: #2980b9;
            transform: translateY(-2px);
        }}
        
        .btn-success {{
            background: #27ae60;
            color: white;
        }}
        
        .btn-success:hover {{
            background: #229954;
            transform: translateY(-2px);
        }}
        
        .btn-danger {{
            background: #e74c3c;
            color: white;
        }}
        
        .btn-danger:hover {{
            background: #c0392b;
            transform: translateY(-2px);
        }}
        
        .social-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin-top: 20px;
        }}
        
        .social-btn {{
            padding: 15px;
            text-align: center;
            border-radius: 10px;
            color: white;
            text-decoration: none;
            font-weight: bold;
            transition: transform 0.3s;
        }}
        
        .social-btn:hover {{
            transform: scale(1.05);
        }}
        
        .whatsapp {{ background: #25d366; }}
        .instagram {{ background: #e4405f; }}
        .facebook {{ background: #1877f2; }}
        .email {{ background: #ea4335; }}
        
        .video-container {{
            text-align: center;
            margin: 20px 0;
        }}
        
        video {{
            width: 100%;
            max-width: 600px;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }}
        
        .footer {{
            text-align: center;
            color: rgba(255,255,255,0.8);
            margin-top: 40px;
            font-size: 14px;
        }}
        
        .status {{
            padding: 10px;
            border-radius: 5px;
            margin: 10px 0;
            text-align: center;
        }}
        
        .status.success {{
            background: #d4edda;
            color: #155724;
            border: 1px solid #c3e6cb;
        }}
        
        .status.error {{
            background: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>💍 Save the Date</h1>
            <p>Prathyusha & Sravan • November 7th, 2025 • 10 AM</p>
            <p>Itihaas Restaurant & Banquet</p>
        </div>
        
        <div class="card">
            <h2>🎬 Your Cinematic Video</h2>
            <div class="video-info">
                <strong>Video Status:</strong> {'✅ Ready to share!' if video_exists else '❌ Not found - please generate first'}<br>
                {'<strong>File Size:</strong> ' + video_size + '<br>' if video_exists else ''}
                <strong>Resolution:</strong> 1920x1080 (Full HD)<br>
                <strong>Duration:</strong> ~18 seconds<br>
                <strong>Format:</strong> MP4 (Social Media Ready)
            </div>
            
            {'''
            <div class="video-container">
                <video controls>
                    <source src="/video" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
            </div>
            ''' if video_exists else ''}
            
            <div style="text-align: center;">
                <a href="/download" class="btn btn-primary">📥 Download Video</a>
                <button onclick="generateVideo()" class="btn btn-success">🎬 Generate Video</button>
            </div>
        </div>
        
        <div class="card">
            <h2>📱 Social Media Sharing</h2>
            <p>Click on any platform below for detailed sharing instructions:</p>
            
            <div class="social-grid">
                <a href="#" onclick="showGuide('whatsapp')" class="social-btn whatsapp">
                    📱 WhatsApp<br><small>Status & Chats</small>
                </a>
                <a href="#" onclick="showGuide('instagram')" class="social-btn instagram">
                    📸 Instagram<br><small>Stories & Feed</small>
                </a>
                <a href="#" onclick="showGuide('facebook')" class="social-btn facebook">
                    📘 Facebook<br><small>Posts & Events</small>
                </a>
                <a href="#" onclick="showGuide('email')" class="social-btn email">
                    📧 Email<br><small>Family & Friends</small>
                </a>
            </div>
        </div>
        
        <div class="card">
            <h2>⚡ Quick Actions</h2>
            <div style="text-align: center;">
                <button onclick="openFolder()" class="btn btn-primary">📁 Open Video Folder</button>
                <a href="https://github.com/srijaharshikad/wedding" target="_blank" class="btn btn-danger">🔗 View on GitHub</a>
            </div>
        </div>
        
        <div class="footer">
            <p>Created with ❤️ for your special day</p>
            <p>GitHub: srijaharshikad/wedding</p>
        </div>
    </div>
    
    <!-- Modal for sharing guides -->
    <div id="modal" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.5); z-index:1000;">
        <div style="position:absolute; top:50%; left:50%; transform:translate(-50%,-50%); background:white; padding:30px; border-radius:15px; max-width:600px; max-height:80%; overflow-y:auto;">
            <span onclick="closeModal()" style="float:right; font-size:24px; cursor:pointer;">&times;</span>
            <div id="modal-content"></div>
        </div>
    </div>

    <script>
        function showGuide(platform) {{
            const guides = {{
                whatsapp: `
                    <h2>📱 WhatsApp Sharing Guide</h2>
                    <h3>For Status:</h3>
                    <ol>
                        <li>Open WhatsApp</li>
                        <li>Tap "Status" at bottom</li>
                        <li>Tap camera icon or "My Status"</li>
                        <li>Select video from gallery</li>
                        <li>Add text: "Save the Date! 💍"</li>
                        <li>Share with all contacts</li>
                    </ol>
                    <h3>For Chats:</h3>
                    <ol>
                        <li>Open any chat or group</li>
                        <li>Tap attachment icon (📎)</li>
                        <li>Select "Gallery" or "Photos"</li>
                        <li>Choose your Save-the-Date video</li>
                        <li>Add caption with wedding details</li>
                        <li>Send to spread the joy!</li>
                    </ol>
                    <p><strong>💡 Tip:</strong> Video is perfect size for WhatsApp (under 30 seconds)</p>
                `,
                instagram: `
                    <h2>📸 Instagram Sharing Guide</h2>
                    <h3>Instagram Stories:</h3>
                    <ol>
                        <li>Open Instagram app</li>
                        <li>Swipe right or tap your profile picture</li>
                        <li>Tap gallery icon (bottom left)</li>
                        <li>Select your video</li>
                        <li>Add stickers: Date, Location, Heart emojis</li>
                        <li>Tag your partner</li>
                        <li>Share to Story</li>
                    </ol>
                    <h3>Instagram Feed:</h3>
                    <ol>
                        <li>Tap + icon at bottom center</li>
                        <li>Select "Post"</li>
                        <li>Choose video from gallery</li>
                        <li>Add caption with hashtags: #SaveTheDate #IndianWedding #November2025</li>
                        <li>Tag people and share</li>
                    </ol>
                `,
                facebook: `
                    <h2>📘 Facebook Sharing Guide</h2>
                    <h3>Facebook Post:</h3>
                    <ol>
                        <li>Open Facebook app</li>
                        <li>Tap "What's on your mind?"</li>
                        <li>Tap "Photo/Video"</li>
                        <li>Select your video</li>
                        <li>Add heartfelt caption with wedding details</li>
                        <li>Tag friends and family</li>
                        <li>Set audience (Public/Friends)</li>
                        <li>Post to share the joy!</li>
                    </ol>
                    <h3>Create Event:</h3>
                    <ol>
                        <li>Go to Events in Facebook</li>
                        <li>Create new event for the wedding</li>
                        <li>Use your video as event cover</li>
                        <li>Invite all your guests!</li>
                    </ol>
                `,
                email: `
                    <h2>📧 Email Sharing Guide</h2>
                    <p><strong>Perfect for older family members!</strong></p>
                    <ol>
                        <li>Open your email app</li>
                        <li>Compose new email</li>
                        <li>Attach the MP4 video file</li>
                        <li>Subject: "Save the Date - Prathyusha & Sravan Wedding"</li>
                        <li>Add message with wedding details</li>
                        <li>Send to family and friends</li>
                    </ol>
                    <h3>Sample Email:</h3>
                    <div style="background:#f8f9fa; padding:15px; border-radius:5px; margin:10px 0;">
                        <p>Dear [Name],</p>
                        <p>We're thrilled to share that Prathyusha and Sravan are getting married! 💍</p>
                        <p><strong>📅 Date:</strong> November 7th, 2025<br>
                        <strong>🕙 Time:</strong> 10:00 AM<br>
                        <strong>📍 Venue:</strong> Itihaas Restaurant & Banquet</p>
                        <p>Please save the date! We've attached a special video announcement.</p>
                        <p>With love,<br>[Your names]</p>
                    </div>
                `
            }};
            
            document.getElementById('modal-content').innerHTML = guides[platform];
            document.getElementById('modal').style.display = 'block';
        }}
        
        function closeModal() {{
            document.getElementById('modal').style.display = 'none';
        }}
        
        function generateVideo() {{
            alert('To generate the video, please run: python3 create_simple_video.py');
        }}
        
        function openFolder() {{
            alert('The video is located in the output/ folder of your project directory.');
        }}
        
        // Close modal when clicking outside
        window.onclick = function(event) {{
            const modal = document.getElementById('modal');
            if (event.target == modal) {{
                modal.style.display = 'none';
            }}
        }}
    </script>
</body>
</html>
        """
    
    def download_video(self):
        """Handle video download"""
        video_path = "output/save_the_date_simple.mp4"
        
        if not os.path.exists(video_path):
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"<h1>Video not found!</h1><p>Please generate the video first.</p>")
            return
        
        # Send the video file
        self.send_response(200)
        self.send_header('Content-type', 'video/mp4')
        self.send_header('Content-Disposition', 'attachment; filename="Prathyusha_Sravan_Save_The_Date.mp4"')
        self.end_headers()
        
        with open(video_path, 'rb') as f:
            shutil.copyfileobj(f, self.wfile)
    
    def serve_video(self):
        """Serve video for preview"""
        video_path = "output/save_the_date_simple.mp4"
        
        if not os.path.exists(video_path):
            self.send_response(404)
            self.end_headers()
            return
        
        self.send_response(200)
        self.send_header('Content-type', 'video/mp4')
        self.end_headers()
        
        with open(video_path, 'rb') as f:
            shutil.copyfileobj(f, self.wfile)
    
    def send_video_info(self):
        """Send video information as JSON"""
        video_path = "output/save_the_date_simple.mp4"
        
        if os.path.exists(video_path):
            size_bytes = os.path.getsize(video_path)
            size_mb = size_bytes / (1024 * 1024)
            
            info = {
                "exists": True,
                "size_mb": round(size_mb, 1),
                "path": video_path,
                "resolution": "1920x1080",
                "duration": "~18 seconds"
            }
        else:
            info = {"exists": False}
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(info).encode())

def start_web_app(port=8080):
    """Start the web application"""
    server_address = ('', port)
    httpd = HTTPServer(server_address, SaveTheDateWebHandler)
    
    print(f"💍 Save the Date Web App")
    print(f"🌐 Starting web server on http://localhost:{port}")
    print(f"📱 Open this URL in your browser to access the app")
    print(f"🛑 Press Ctrl+C to stop the server")
    
    # Open browser automatically after a short delay
    def open_browser():
        time.sleep(1)
        webbrowser.open(f'http://localhost:{port}')
    
    browser_thread = threading.Thread(target=open_browser)
    browser_thread.daemon = True
    browser_thread.start()
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n👋 Shutting down web server...")
        httpd.shutdown()

if __name__ == "__main__":
    start_web_app()
