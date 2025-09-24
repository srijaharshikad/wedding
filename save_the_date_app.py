#!/usr/bin/env python3
"""
Save the Date - User Friendly Download App
A simple GUI application for Prathyusha & Sravan's wedding video
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os
import shutil
import subprocess
import webbrowser
from pathlib import Path
import platform

class SaveTheDateApp:
    def __init__(self, root):
        self.root = root
        self.root.title("💍 Prathyusha & Sravan - Save the Date")
        self.root.geometry("600x700")
        self.root.configure(bg='#f5f5f5')
        
        # Set window icon (if available)
        try:
            self.root.iconbitmap('assets/icon.ico')
        except:
            pass
        
        self.video_path = "output/save_the_date_simple.mp4"
        self.setup_ui()
        
    def setup_ui(self):
        """Create the user interface"""
        
        # Header
        header_frame = tk.Frame(self.root, bg='#2c3e50', height=100)
        header_frame.pack(fill='x', padx=0, pady=0)
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(
            header_frame, 
            text="💍 Save the Date", 
            font=('Georgia', 24, 'bold'),
            fg='white', 
            bg='#2c3e50'
        )
        title_label.pack(pady=10)
        
        couple_label = tk.Label(
            header_frame,
            text="Prathyusha & Sravan • November 7th, 2025",
            font=('Georgia', 14),
            fg='#ecf0f1',
            bg='#2c3e50'
        )
        couple_label.pack()
        
        # Main content frame
        main_frame = tk.Frame(self.root, bg='#f5f5f5')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Video info section
        info_frame = tk.LabelFrame(
            main_frame, 
            text="🎬 Video Information", 
            font=('Arial', 12, 'bold'),
            bg='#f5f5f5',
            fg='#2c3e50'
        )
        info_frame.pack(fill='x', pady=(0, 15))
        
        self.create_video_info(info_frame)
        
        # Download section
        download_frame = tk.LabelFrame(
            main_frame,
            text="📥 Download Video",
            font=('Arial', 12, 'bold'),
            bg='#f5f5f5',
            fg='#2c3e50'
        )
        download_frame.pack(fill='x', pady=(0, 15))
        
        self.create_download_section(download_frame)
        
        # Social media section
        social_frame = tk.LabelFrame(
            main_frame,
            text="📱 Share on Social Media",
            font=('Arial', 12, 'bold'),
            bg='#f5f5f5',
            fg='#2c3e50'
        )
        social_frame.pack(fill='x', pady=(0, 15))
        
        self.create_social_section(social_frame)
        
        # Actions section
        actions_frame = tk.LabelFrame(
            main_frame,
            text="⚡ Quick Actions",
            font=('Arial', 12, 'bold'),
            bg='#f5f5f5',
            fg='#2c3e50'
        )
        actions_frame.pack(fill='x', pady=(0, 15))
        
        self.create_actions_section(actions_frame)
        
        # Footer
        footer_frame = tk.Frame(self.root, bg='#34495e', height=50)
        footer_frame.pack(fill='x', side='bottom')
        footer_frame.pack_propagate(False)
        
        footer_label = tk.Label(
            footer_frame,
            text="Created with ❤️ for your special day | GitHub: srijaharshikad/wedding",
            font=('Arial', 10),
            fg='white',
            bg='#34495e'
        )
        footer_label.pack(pady=15)
        
    def create_video_info(self, parent):
        """Create video information display"""
        info_text = tk.Text(
            parent, 
            height=4, 
            bg='white', 
            fg='#2c3e50',
            font=('Courier', 10),
            wrap='word',
            state='disabled'
        )
        info_text.pack(fill='x', padx=10, pady=10)
        
        # Get video info
        video_info = self.get_video_info()
        
        info_text.config(state='normal')
        info_text.insert('1.0', video_info)
        info_text.config(state='disabled')
        
    def create_download_section(self, parent):
        """Create download buttons and options"""
        
        # Download to Downloads folder
        downloads_btn = tk.Button(
            parent,
            text="📁 Download to Downloads Folder",
            font=('Arial', 11, 'bold'),
            bg='#3498db',
            fg='white',
            padx=20,
            pady=10,
            command=self.download_to_downloads
        )
        downloads_btn.pack(pady=10)
        
        # Choose custom location
        custom_btn = tk.Button(
            parent,
            text="📂 Choose Download Location",
            font=('Arial', 11),
            bg='#95a5a6',
            fg='white',
            padx=20,
            pady=8,
            command=self.download_custom_location
        )
        custom_btn.pack(pady=5)
        
    def create_social_section(self, parent):
        """Create social media sharing options"""
        
        # Create a frame for buttons
        buttons_frame = tk.Frame(parent, bg='#f5f5f5')
        buttons_frame.pack(pady=10)
        
        # WhatsApp
        whatsapp_btn = tk.Button(
            buttons_frame,
            text="📱 WhatsApp Guide",
            font=('Arial', 10, 'bold'),
            bg='#25d366',
            fg='white',
            padx=15,
            pady=8,
            command=self.show_whatsapp_guide
        )
        whatsapp_btn.grid(row=0, column=0, padx=5, pady=5)
        
        # Instagram
        instagram_btn = tk.Button(
            buttons_frame,
            text="📸 Instagram Guide",
            font=('Arial', 10, 'bold'),
            bg='#e4405f',
            fg='white',
            padx=15,
            pady=8,
            command=self.show_instagram_guide
        )
        instagram_btn.grid(row=0, column=1, padx=5, pady=5)
        
        # Facebook
        facebook_btn = tk.Button(
            buttons_frame,
            text="📘 Facebook Guide",
            font=('Arial', 10, 'bold'),
            bg='#1877f2',
            fg='white',
            padx=15,
            pady=8,
            command=self.show_facebook_guide
        )
        facebook_btn.grid(row=1, column=0, padx=5, pady=5)
        
        # Email
        email_btn = tk.Button(
            buttons_frame,
            text="📧 Email Guide",
            font=('Arial', 10, 'bold'),
            bg='#ea4335',
            fg='white',
            padx=15,
            pady=8,
            command=self.show_email_guide
        )
        email_btn.grid(row=1, column=1, padx=5, pady=5)
        
    def create_actions_section(self, parent):
        """Create quick action buttons"""
        
        actions_frame = tk.Frame(parent, bg='#f5f5f5')
        actions_frame.pack(pady=10)
        
        # Play video
        play_btn = tk.Button(
            actions_frame,
            text="▶️ Preview Video",
            font=('Arial', 11, 'bold'),
            bg='#e74c3c',
            fg='white',
            padx=20,
            pady=8,
            command=self.play_video
        )
        play_btn.grid(row=0, column=0, padx=10, pady=5)
        
        # Open folder
        folder_btn = tk.Button(
            actions_frame,
            text="📁 Open Video Folder",
            font=('Arial', 11),
            bg='#f39c12',
            fg='white',
            padx=20,
            pady=8,
            command=self.open_video_folder
        )
        folder_btn.grid(row=0, column=1, padx=10, pady=5)
        
        # GitHub link
        github_btn = tk.Button(
            actions_frame,
            text="🔗 View on GitHub",
            font=('Arial', 11),
            bg='#2c3e50',
            fg='white',
            padx=20,
            pady=8,
            command=self.open_github
        )
        github_btn.grid(row=1, column=0, columnspan=2, pady=5)
        
    def get_video_info(self):
        """Get video file information"""
        if os.path.exists(self.video_path):
            file_size = os.path.getsize(self.video_path)
            file_size_mb = file_size / (1024 * 1024)
            
            return f"""🎬 File: {self.video_path}
📏 Size: {file_size_mb:.1f} MB
🎯 Resolution: 1920x1080 (Full HD)
⏱️ Duration: ~18 seconds
📱 Social Media Ready: ✅"""
        else:
            return "❌ Video file not found! Please generate the video first."
    
    def download_to_downloads(self):
        """Download video to Downloads folder"""
        if not os.path.exists(self.video_path):
            messagebox.showerror("Error", "Video file not found! Please generate the video first.")
            return
        
        downloads_path = Path.home() / "Downloads"
        destination = downloads_path / "Prathyusha_Sravan_Save_The_Date.mp4"
        
        try:
            shutil.copy2(self.video_path, destination)
            messagebox.showinfo(
                "Success! 🎉", 
                f"Video downloaded successfully!\n\n📁 Location: {destination}\n\n📱 Ready to share on social media!"
            )
        except Exception as e:
            messagebox.showerror("Error", f"Failed to download video: {e}")
    
    def download_custom_location(self):
        """Download video to custom location"""
        if not os.path.exists(self.video_path):
            messagebox.showerror("Error", "Video file not found! Please generate the video first.")
            return
        
        destination = filedialog.asksaveasfilename(
            defaultextension=".mp4",
            filetypes=[("MP4 files", "*.mp4"), ("All files", "*.*")],
            initialname="Prathyusha_Sravan_Save_The_Date.mp4"
        )
        
        if destination:
            try:
                shutil.copy2(self.video_path, destination)
                messagebox.showinfo(
                    "Success! 🎉", 
                    f"Video saved successfully!\n\n📁 Location: {destination}\n\n📱 Ready to share!"
                )
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save video: {e}")
    
    def show_whatsapp_guide(self):
        """Show WhatsApp sharing guide"""
        guide = """📱 WhatsApp Sharing Guide:

FOR STATUS:
1. Open WhatsApp
2. Tap "Status" at bottom
3. Tap camera icon or "My Status"
4. Select video from gallery
5. Add text: "Save the Date! 💍"
6. Share with all contacts

FOR CHATS:
1. Open any chat or group
2. Tap attachment icon (📎)
3. Select "Gallery" or "Photos"
4. Choose your Save-the-Date video
5. Add caption with wedding details
6. Send to spread the joy!

💡 Tip: Video is perfect size for WhatsApp (under 30 seconds)"""
        
        messagebox.showinfo("WhatsApp Sharing Guide 📱", guide)
    
    def show_instagram_guide(self):
        """Show Instagram sharing guide"""
        guide = """📸 Instagram Sharing Guide:

INSTAGRAM STORIES:
1. Open Instagram app
2. Swipe right or tap your profile picture
3. Tap gallery icon (bottom left)
4. Select your video
5. Add stickers: Date, Location, Heart emojis
6. Tag your partner
7. Share to Story

INSTAGRAM FEED:
1. Tap + icon at bottom center
2. Select "Post"
3. Choose video from gallery
4. Add caption with hashtags:
   #SaveTheDate #IndianWedding #November2025
5. Tag people and share

INSTAGRAM REELS:
1. Tap Reels at bottom
2. Upload your video
3. Add trending wedding music
4. Use wedding hashtags
5. Share to reach more people!"""
        
        messagebox.showinfo("Instagram Sharing Guide 📸", guide)
    
    def show_facebook_guide(self):
        """Show Facebook sharing guide"""
        guide = """📘 Facebook Sharing Guide:

FACEBOOK POST:
1. Open Facebook app
2. Tap "What's on your mind?"
3. Tap "Photo/Video"
4. Select your video
5. Add heartfelt caption with wedding details
6. Tag friends and family
7. Set audience (Public/Friends)
8. Post to share the joy!

FACEBOOK STORY:
1. Tap "Add to Story" at top
2. Select your video
3. Add text or stickers
4. Share to Story

CREATE EVENT:
1. Go to Events in Facebook
2. Create new event for the wedding
3. Use your video as event cover
4. Invite all your guests!

💡 Perfect for reaching extended family and friends"""
        
        messagebox.showinfo("Facebook Sharing Guide 📘", guide)
    
    def show_email_guide(self):
        """Show email sharing guide"""
        guide = """📧 Email Sharing Guide:

PERFECT FOR OLDER FAMILY MEMBERS:

1. Open your email app
2. Compose new email
3. Attach the MP4 video file
4. Subject: "Save the Date - Prathyusha & Sravan Wedding"
5. Add message:

"Dear [Name],

We're thrilled to share that Prathyusha and Sravan are getting married! 💍

📅 Date: November 7th, 2025
🕙 Time: 10:00 AM  
📍 Venue: Itihaas Restaurant & Banquet

Please save the date! We've attached a special video announcement.

Formal invitations will follow soon.

With love,
[Your names]"

6. Send to family and friends

💡 Great for those who don't use social media!"""
        
        messagebox.showinfo("Email Sharing Guide 📧", guide)
    
    def play_video(self):
        """Play the video using default player"""
        if not os.path.exists(self.video_path):
            messagebox.showerror("Error", "Video file not found! Please generate the video first.")
            return
        
        try:
            if platform.system() == 'Darwin':  # macOS
                subprocess.run(['open', self.video_path])
            elif platform.system() == 'Windows':  # Windows
                os.startfile(self.video_path)
            else:  # Linux
                subprocess.run(['xdg-open', self.video_path])
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open video: {e}")
    
    def open_video_folder(self):
        """Open the folder containing the video"""
        try:
            folder_path = os.path.dirname(os.path.abspath(self.video_path))
            if platform.system() == 'Darwin':  # macOS
                subprocess.run(['open', folder_path])
            elif platform.system() == 'Windows':  # Windows
                os.startfile(folder_path)
            else:  # Linux
                subprocess.run(['xdg-open', folder_path])
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open folder: {e}")
    
    def open_github(self):
        """Open GitHub repository"""
        webbrowser.open("https://github.com/srijaharshikad/wedding")

def main():
    """Run the application"""
    root = tk.Tk()
    app = SaveTheDateApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
