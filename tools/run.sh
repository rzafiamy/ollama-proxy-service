#!/bin/bash

# Default paths
VENV_PATH=${1:-$(pwd)/.pyenv}
WORKING_DIRECTORY=${2:-$(pwd)}
APP_MODULE="app:app"  # Adjust if your entry point is different
PORT=${PORT:-11433}   # Default port, can be overridden by setting $PORT
WORKERS=${WORKERS:-4} # Default Gunicorn workers, can be overridden

echo "🔧 Setting up the environment..."

# Create virtual environment if it does not exist
if [ ! -d "$VENV_PATH" ]; then
    echo "🛠 Creating virtual environment in $VENV_PATH..."
    python3 -m venv "$VENV_PATH"
fi

# Activate virtual environment
echo "🚀 Activating virtual environment..."
source "$VENV_PATH/bin/activate"

# Ensure dependencies are installed
echo "📦 Installing required packages..."
pip install --upgrade pip
pip install -r requirements.txt

# Move to working directory
cd "$WORKING_DIRECTORY" || exit

# Check if Gunicorn is installed, install if missing
if ! command -v gunicorn &>/dev/null; then
    echo "⚠️ Gunicorn not found. Installing..."
    pip install gunicorn
fi

# Kill previous Gunicorn process if running
PID_FILE="$WORKING_DIRECTORY/gunicorn.pid"
if [ -f "$PID_FILE" ]; then
    echo "🛑 Stopping previous Gunicorn process..."
    kill -9 $(cat "$PID_FILE") 2>/dev/null
    rm -f "$PID_FILE"
fi

# Start Gunicorn
echo "🚀 Starting Gunicorn with $WORKERS workers on port $PORT..."
gunicorn -w "$WORKERS" -b 0.0.0.0:"$PORT" --timeout 500 --error-logfile "$APP_MODULE" 

echo "✅ Flask app running on http://localhost:$PORT"
