# Ollama Proxy Service

### 🚨 Secure Your Data with Ease!

This repository showcases how to protect your Ollama instance using Flask, Flask-Limiter, and Flask-Cors. With this setup, you can ensure robust API key security and safeguard your valuable data.

### Features

    🔒 API key protection with Flask
    🕵️‍♀️ Rate limiting using Flask-Limiter
    💻 Cross-origin resource sharing with Flask-Cors

### Table of Contents

*   [Overview](#overview)
*   [Installation](#installation)
*   [Usage](#usage)
*   [API Documentation](#api-documentation)
*   [Troubleshooting](#troubleshooting)

## Overview
--------

This is a lightweight proxy service that protects Ollama with an API key. It uses Flask as the web framework, Flask-Limiter for rate limiting, and Flask-Cors for enabling cross-origin resource sharing.

## Installation
------------

To install this service, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/ollama-proxy-service.git
    cd ollama-proxy-service
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up the service using the setup script:
    ```bash
    ./setup.sh install
    ```

This will create necessary user and group for the service, and configure the systemd service to manage the application.

## Usage
-----

### Running the Service

To start the service and manage it through systemd, use:

```bash
sudo systemctl start ollama-proxy-service.service
```

For development or manual testing, you can run the service directly:

```bash
./run.sh
```

This will ensure the virtual environment is set up and start the Flask application on the default port 11433. Access it by visiting `http://localhost:11433` in your browser.

### API Key

To protect Ollama with an API key, set the `API_KEY` variable in the `config.py` file:

```python
# config.py
API_KEY = "your_api_key_here"
```

Ensure that only requests with a valid API key can access Ollama.

## API Documentation
-------------------

### API Endpoints

The proxy service supports all standard HTTP methods (GET, POST, PUT, DELETE) and has one endpoint `/` that proxies requests to the target URL (`http://localhost:11434` by default).

### API Keys

Include the `Authorization` header with a value of `Bearer <API_KEY>` in your request to authenticate. Valid API keys will proceed with the expected response, while invalid ones will result in a 401 Unauthorized error.

## Troubleshooting
--------------

*   **Error streaming response**: Verify that the target URL is responding properly and that there are no network issues.
*   **Invalid API key**: Confirm that the `API_KEY` variable in `config.py` is set correctly.

## Thanks

Special Thanks

This project wouldn't have been possible without the inspiration and guidance from @rzafiamy! His expertise and kindness made a huge difference, and I'm grateful for his contributions. 🙏💖