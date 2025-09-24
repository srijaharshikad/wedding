#!/bin/bash
# Save the Date App Launcher for Linux
# Run: chmod +x run_app.sh && ./run_app.sh

echo "💍 Prathyusha & Sravan - Save the Date App"
echo "🚀 Starting application..."

# Get the directory where this script is located
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd "$DIR"

# Check if Python 3 is installed
if command -v python3 &> /dev/null; then
    echo "✅ Python 3 found"
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    echo "✅ Python found"
    PYTHON_CMD="python"
else
    echo "❌ Python not found!"
    echo "Please install Python 3:"
    echo "Ubuntu/Debian: sudo apt install python3 python3-pip python3-tk"
    echo "CentOS/RHEL: sudo yum install python3 python3-pip tkinter"
    echo "Arch: sudo pacman -S python python-pip tk"
    read -p "Press Enter to exit..."
    exit 1
fi

# Install requirements if needed
if [ ! -f ".requirements_installed" ]; then
    echo "📦 Installing required packages..."
    $PYTHON_CMD -m pip install --user -r requirements.txt
    if [ $? -eq 0 ]; then
        touch .requirements_installed
        echo "✅ Packages installed successfully"
    else
        echo "❌ Failed to install packages"
        echo "You might need to install tkinter separately:"
        echo "sudo apt install python3-tk  # Ubuntu/Debian"
        read -p "Press Enter to continue anyway..."
    fi
fi

# Run the app
echo "🎬 Launching Save the Date App..."
$PYTHON_CMD run_app.py

echo "👋 Thank you for using Save the Date App!"
read -p "Press Enter to close..."
