#!/bin/bash

# Prework Study Guide - Quick Installation Script

echo "🎓 Prework Study Guide Installation"
echo "==================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.7 or higher."
    exit 1
fi

# Check Python version
python_version=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "✅ Found Python $python_version"

# Check if pip is available
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip."
    exit 1
fi

echo "✅ Found pip3"

# Install dependencies
echo ""
echo "📦 Installing dependencies..."
pip3 install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed successfully!"
else
    echo "❌ Failed to install dependencies."
    exit 1
fi

# Make the script executable
chmod +x quiz_app.py

echo ""
echo "🎉 Installation complete!"
echo ""
echo "To start the quiz, run:"
echo "    python3 quiz_app.py"
echo ""
echo "Or if you want to install it globally:"
echo "    pip3 install -e ."
echo "    study-quiz"
echo ""
echo "Happy studying! 📚"