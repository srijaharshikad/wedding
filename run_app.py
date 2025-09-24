#!/usr/bin/env python3
"""
Simple launcher for the Save the Date App
This ensures the app runs from the correct directory
"""

import os
import sys
from pathlib import Path

def main():
    """Launch the Save the Date App"""
    
    # Get the directory where this script is located
    script_dir = Path(__file__).parent.absolute()
    
    # Change to the script directory
    os.chdir(script_dir)
    
    # Check if video exists, if not, offer to create it
    video_path = "output/save_the_date_simple.mp4"
    
    if not os.path.exists(video_path):
        print("🎬 Video not found! Creating your Save-the-Date video...")
        print("This will take a few moments...")
        
        try:
            import subprocess
            result = subprocess.run([sys.executable, "create_simple_video.py"], 
                                  capture_output=True, text=True)
            
            if result.returncode == 0:
                print("✅ Video created successfully!")
            else:
                print("❌ Error creating video:")
                print(result.stderr)
                input("Press Enter to continue anyway...")
        except Exception as e:
            print(f"❌ Error: {e}")
            input("Press Enter to continue...")
    
    # Launch the GUI app
    try:
        from save_the_date_app import main as app_main
        app_main()
    except ImportError as e:
        print(f"❌ Error importing app: {e}")
        print("Make sure you're running this from the wedding directory")
        input("Press Enter to exit...")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()
