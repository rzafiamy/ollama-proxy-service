#!/bin/bash

# Configuration defaults
USERNAME=${1:-ollama_user}
GROUP=${2:-ollama_group}
WORKING_DIRECTORY=${3:-$(pwd)}
VENV_PATH=${4:-$(pwd)/.pyenv}

# Functions
create_user() {
    if id "$USERNAME" &>/dev/null; then
        echo "User $USERNAME already exists."
    else
        sudo useradd -r -s /bin/false $USERNAME
        sudo groupadd $GROUP
        sudo usermod -a -G $GROUP $USERNAME
    fi
}

install_service() {
    create_user
    sudo cp ollama-proxy-service.service.tpl /etc/systemd/system/ollama-proxy-service.service
    sudo sed -i "s|{{USERNAME}}|$USERNAME|g" /etc/systemd/system/ollama-proxy-service.service
    sudo sed -i "s|{{GROUP}}|$GROUP|g" /etc/systemd/system/ollama-proxy-service.service
    sudo sed -i "s|{{WORKING_DIRECTORY}}|$WORKING_DIRECTORY|g" /etc/systemd/system/ollama-proxy-service.service
    sudo sed -i "s|{{VENV_PATH}}|$VENV_PATH|g" /etc/systemd/system/ollama-proxy-service.service
    sudo systemctl daemon-reload
    sudo systemctl enable ollama-proxy-service.service
    echo "Service installed and enabled."
}

uninstall_service() {
    sudo systemctl stop ollama-proxy-service.service
    sudo systemctl disable ollama-proxy-service.service
    sudo rm /etc/systemd/system/ollama-proxy-service.service
    sudo systemctl daemon-reload
    echo "Service uninstalled."
}

# Main execution flow
case "$5" in
    install)
        install_service
        ;;
    uninstall)
        uninstall_service
        ;;
    *)
        echo "Usage: $0 [username] [group] [working directory] [venv path] {install|uninstall}"
        exit 1
        ;;
esac
