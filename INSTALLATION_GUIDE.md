# 📱 Save the Date App - Installation Guide

## 🚀 Quick Start (Easiest Method)

### Option 1: Direct Download from GitHub
1. **Download the project**:
   - Go to: https://github.com/srijaharshikad/wedding
   - Click the green "Code" button
   - Select "Download ZIP"
   - Extract the ZIP file to your desired location

2. **Run the app**:
   - **Windows**: Double-click `run_app.bat`
   - **Mac**: Double-click `run_app.command`  
   - **Linux**: Run `./run_app.sh` in terminal

### Option 2: Clone with Git
```bash
git clone https://github.com/srijaharshikad/wedding.git
cd wedding
python3 run_app.py
```

---

## 🖥️ User-Friendly Desktop App

The app provides a beautiful, easy-to-use interface with:

### 📋 Features:
- **🎬 Video Preview**: Watch your Save-the-Date video
- **📥 One-Click Download**: Download to Downloads folder or custom location
- **📱 Social Media Guides**: Step-by-step sharing instructions for:
  - WhatsApp (Status & Chats)
  - Instagram (Stories, Feed, Reels)
  - Facebook (Posts, Stories, Events)
  - Email (for family members)
- **⚡ Quick Actions**: Preview video, open folder, view on GitHub

### 🎯 Perfect For:
- **Non-technical users** who want a simple interface
- **Family members** who need help with social media sharing
- **Quick downloads** without command line
- **Step-by-step guidance** for each platform

---

## 💻 System Requirements

### Minimum Requirements:
- **Operating System**: Windows 10+, macOS 10.14+, or Linux
- **Python**: 3.7 or higher (usually pre-installed on Mac/Linux)
- **RAM**: 4GB minimum, 8GB recommended
- **Storage**: 500MB free space
- **Internet**: Required for initial download only

### Python Libraries (Auto-installed):
- `tkinter` (GUI framework - usually included with Python)
- `opencv-python` (video processing)
- `pillow` (image processing)
- `numpy` (mathematical operations)

---

## 🔧 Installation Methods

### Method 1: Automatic Installation (Recommended)

#### For Windows Users:
1. Download the project ZIP from GitHub
2. Extract to `C:\SaveTheDate\` (or any folder)
3. Double-click `install_windows.bat`
4. The installer will:
   - Check for Python
   - Install required packages
   - Create desktop shortcut
   - Launch the app

#### For Mac Users:
1. Download the project ZIP from GitHub
2. Extract to `~/SaveTheDate/` (or any folder)
3. Double-click `install_mac.command`
4. The installer will:
   - Check for Python 3
   - Install required packages using pip
   - Create app in Applications folder
   - Launch the app

#### For Linux Users:
1. Download and extract the project
2. Open terminal in the project folder
3. Run: `chmod +x install_linux.sh && ./install_linux.sh`
4. The installer will handle everything automatically

### Method 2: Manual Installation

#### Step 1: Install Python (if not already installed)
- **Windows**: Download from https://python.org
- **Mac**: Usually pre-installed, or use `brew install python3`
- **Linux**: `sudo apt install python3 python3-pip` (Ubuntu/Debian)

#### Step 2: Install Required Packages
```bash
pip3 install opencv-python pillow numpy
```

#### Step 3: Download Project
```bash
git clone https://github.com/srijaharshikad/wedding.git
cd wedding
```

#### Step 4: Run the App
```bash
python3 run_app.py
```

---

## 🎮 How to Use the App

### 1. **Launch the App**
   - Use one of the installation methods above
   - The app will automatically create the video if it doesn't exist

### 2. **Download Your Video**
   - Click "📁 Download to Downloads Folder" for quick access
   - Or click "📂 Choose Download Location" to save anywhere
   - The video will be named: `Prathyusha_Sravan_Save_The_Date.mp4`

### 3. **Share on Social Media**
   - Click any social media button for detailed instructions
   - Follow the step-by-step guides for each platform
   - Each guide is tailored for that specific app

### 4. **Quick Actions**
   - **▶️ Preview Video**: Watch your video before sharing
   - **📁 Open Video Folder**: Access the video files directly
   - **🔗 View on GitHub**: Visit the project repository

---

## 📱 Social Media Sharing Made Easy

### WhatsApp 📱
- **Status**: Perfect for 24-hour announcements
- **Groups**: Share with family and friend groups
- **Individual Chats**: Personal invitations

### Instagram 📸
- **Stories**: Add stickers, location tags, and music
- **Feed Posts**: Permanent announcement with hashtags
- **Reels**: Reach a wider audience with trending sounds

### Facebook 📘
- **Posts**: Share with friends and family
- **Stories**: 24-hour announcements
- **Events**: Create a wedding event page

### Email 📧
- **Perfect for older family members**
- **Professional invitations**
- **Detailed wedding information**

---

## 🔧 Troubleshooting

### Common Issues:

#### "Python not found"
- **Solution**: Install Python from https://python.org
- Make sure to check "Add Python to PATH" during installation

#### "Module not found" errors
- **Solution**: Run `pip3 install -r requirements.txt`
- Or use the automatic installers

#### Video not generating
- **Solution**: 
  - Check internet connection
  - Ensure you have enough disk space (500MB)
  - Try running `python3 create_simple_video.py` manually

#### App won't start on Mac
- **Solution**: 
  - Right-click the file → "Open With" → "Terminal"
  - Or run `chmod +x run_app.command` in terminal

#### GUI looks strange/doesn't display properly
- **Solution**: 
  - Update your system
  - Try running: `python3 -m tkinter` to test GUI support
  - On Linux: `sudo apt install python3-tk`

---

## 🆘 Getting Help

### If you need assistance:

1. **Check the GitHub Issues**: https://github.com/srijaharshikad/wedding/issues
2. **Create a new issue** with:
   - Your operating system
   - Python version (`python3 --version`)
   - Error message (if any)
   - What you were trying to do

3. **Contact Information**:
   - GitHub: @srijaharshikad
   - Email: Include in your GitHub issue

---

## 🎉 Success!

Once installed, you'll have:
- ✅ Beautiful desktop app for easy video access
- ✅ One-click download functionality  
- ✅ Step-by-step social media guides
- ✅ Professional Save-the-Date video ready to share
- ✅ All files organized and accessible

**Your cinematic Save-the-Date announcement is ready to share with the world! 💍✨**

---

## 📋 Quick Reference

### File Structure:
```
wedding/
├── save_the_date_app.py          # Main GUI application
├── run_app.py                    # App launcher
├── create_simple_video.py        # Video generator
├── output/                       # Generated videos
├── requirements.txt              # Python dependencies
├── README.md                     # Project documentation
├── SOCIAL_MEDIA_GUIDE.md         # Detailed sharing guide
└── INSTALLATION_GUIDE.md         # This file
```

### Key Commands:
- **Run App**: `python3 run_app.py`
- **Generate Video**: `python3 create_simple_video.py`
- **Install Dependencies**: `pip3 install -r requirements.txt`

**Happy sharing! 🎊**
