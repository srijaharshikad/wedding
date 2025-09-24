#!/usr/bin/env python3
"""
Video Download Helper for Save-the-Date
Simple script to help download and share the video
"""

import os
import shutil
from pathlib import Path

def download_video():
    """Copy video to Downloads folder for easy access"""
    video_path = "output/save_the_date_simple.mp4"
    
    if not os.path.exists(video_path):
        print("❌ Video not found! Please run create_simple_video.py first.")
        return
    
    # Get user's Downloads folder
    downloads_path = Path.home() / "Downloads"
    destination = downloads_path / "Prathyusha_Sravan_Save_The_Date.mp4"
    
    try:
        shutil.copy2(video_path, destination)
        print(f"✅ Video copied to Downloads folder!")
        print(f"📁 Location: {destination}")
        print(f"📱 Ready to share on social media!")
        
        # Print quick sharing tips
        print("\n🚀 Quick Sharing Tips:")
        print("📱 WhatsApp: Attach from Downloads folder")
        print("📸 Instagram: Upload to Stories or Feed")
        print("📘 Facebook: Create a post and upload video")
        print("📧 Email: Attach for older family members")
        
        return str(destination)
        
    except Exception as e:
        print(f"❌ Error copying video: {e}")
        return None

def get_video_info():
    """Display video information"""
    video_path = "output/save_the_date_simple.mp4"
    
    if os.path.exists(video_path):
        file_size = os.path.getsize(video_path)
        file_size_mb = file_size / (1024 * 1024)
        
        print(f"🎬 Video Information:")
        print(f"📁 File: {video_path}")
        print(f"📏 Size: {file_size_mb:.1f} MB")
        print(f"🎯 Resolution: 1920x1080 (Full HD)")
        print(f"🎵 Duration: ~18 seconds")
        print(f"📱 Social Media Ready: ✅")
        
    else:
        print("❌ Video not found!")

if __name__ == "__main__":
    print("💍 Prathyusha & Sravan - Save the Date Video")
    print("📥 Video Download Helper\n")
    
    get_video_info()
    print("\n" + "="*50 + "\n")
    download_video()
