#!/bin/bash

# Define the service and installation URL
SERVICE="ollama.service"
INSTALL_URL="https://ollama.com/install.sh"

# Step 1: Install or update Ollama using the provided command
echo "Installing or updating Ollama..."
curl -fsSL $INSTALL_URL | sh

# Step 2: Check if the systemd service exists and modify the environment settings
SERVICE_PATH="/etc/systemd/system/$SERVICE"
if [ -f "$SERVICE_PATH" ]; then
    echo "Updating $SERVICE environment settings..."
    # Ensure the Environment lines exist, add if not
    if ! grep -q 'Environment="OLLAMA_HOST=' $SERVICE_PATH; then
        sudo sed -i '/\[Service\]/a Environment="OLLAMA_HOST=0.0.0.0:11434"' $SERVICE_PATH
    else
        sudo sed -i '/Environment="OLLAMA_HOST=/c\Environment="OLLAMA_HOST=0.0.0.0:11434"' $SERVICE_PATH
    fi

    if ! grep -q 'Environment="OLLAMA_ORIGINS=' $SERVICE_PATH; then
        sudo sed -i '/\[Service\]/a Environment="OLLAMA_ORIGINS=*"' $SERVICE_PATH
    else
        sudo sed -i '/Environment="OLLAMA_ORIGINS=/c\Environment="OLLAMA_ORIGINS=*"' $SERVICE_PATH
    fi

    # Step 3: Reload systemd to apply changes
    echo "Reloading systemd daemon..."
    sudo systemctl daemon-reload

    # Step 4: Restart the service to apply new settings
    echo "Restarting $SERVICE..."
    sudo systemctl restart $SERVICE
else
    echo "Error: $SERVICE does not exist."
fi

echo "Ollama update and configuration script completed."