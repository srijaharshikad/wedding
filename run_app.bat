@echo off
REM Save the Date App Launcher for Windows
REM Double-click this file to run the app

title Prathyusha & Sravan - Save the Date App

echo 💍 Prathyusha ^& Sravan - Save the Date App
echo 🚀 Starting application...
echo.

REM Change to the script directory
cd /d "%~dp0"

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ Python found
    set PYTHON_CMD=python
) else (
    python3 --version >nul 2>&1
    if %errorlevel% equ 0 (
        echo ✅ Python 3 found
        set PYTHON_CMD=python3
    ) else (
        echo ❌ Python not found!
        echo Please install Python 3 from https://python.org
        echo Make sure to check "Add Python to PATH" during installation
        pause
        exit /b 1
    )
)

REM Install requirements if needed
if not exist ".requirements_installed" (
    echo 📦 Installing required packages...
    %PYTHON_CMD% -m pip install --user -r requirements.txt
    if %errorlevel% equ 0 (
        echo. > .requirements_installed
        echo ✅ Packages installed successfully
    ) else (
        echo ❌ Failed to install packages
        echo Press any key to continue anyway...
        pause >nul
    )
)

REM Run the app
echo 🎬 Launching Save the Date App...
echo.
%PYTHON_CMD% run_app.py

echo.
echo 👋 Thank you for using Save the Date App!
pause
