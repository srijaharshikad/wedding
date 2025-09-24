#!/bin/bash
# Save the Date App Launcher for Mac
# Double-click this file to run the app

echo "💍 Prathyusha & Sravan - Save the Date App"
echo "🚀 Starting application..."

# Get the directory where this script is located
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd "$DIR"

# Check if Python 3 is installed
if command -v python3 &> /dev/null; then
    echo "✅ Python 3 found"
elif command -v python &> /dev/null; then
    echo "✅ Python found"
    python3="python"
else
    echo "❌ Python not found!"
    echo "Please install Python 3 from https://python.org"
    read -p "Press Enter to exit..."
    exit 1
fi

# Install requirements if needed
if [ ! -f ".requirements_installed" ]; then
    echo "📦 Installing required packages..."
    python3 -m pip install --user -r requirements.txt
    if [ $? -eq 0 ]; then
        touch .requirements_installed
        echo "✅ Packages installed successfully"
    else
        echo "❌ Failed to install packages"
        read -p "Press Enter to continue anyway..."
    fi
fi

# Run the app
echo "🎬 Launching Save the Date App..."
python3 run_app.py

echo "👋 Thank you for using Save the Date App!"
read -p "Press Enter to close..."
