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

This is a lightweight proxy service that protects ollama with an API key. It uses Flask as the web framework, Flask-Limiter for rate limiting, and Flask-Cors for enabling cross-origin resource sharing.

## Installation
------------

To install this service, simply clone the repository using git and run `pip install -r requirements.txt` to install the required dependencies.

```bash
git clone https://github.com/your-repo-url.git
cd your-repo-name
pip install -r requirements.txt
```

## Usage
-----

### Running the Service

To start the service, simply run:

```bash
python proxy.py
```

This will start the proxy service on port 11433. You can access it by visiting `http://localhost:11433` in your browser.

### API Key

To protect ollama with an API key, you need to set the `API_KEY` variable in the `config.py` file to your desired API key. This will ensure that only requests with a valid API key can access ollama.

```python
# config.py
API_KEY = "your_api_key_here"
```

## API Documentation
-------------------

### API Endpoints

The proxy service supports all standard HTTP methods (GET, POST, PUT, DELETE) and has one endpoint `/` that proxies requests to the target URL (`http://localhost:11434` by default).

### API Keys

To authenticate with an API key, you need to include the `Authorization` header in your request with a value of `Bearer <API_KEY>`. If the API key is valid, the response will be sent as expected. Otherwise, a 401 Unauthorized error will be returned.

## Troubleshooting
--------------

*   **Error streaming response**: Check if the target URL is responding correctly and if there are any network issues.
*   **Invalid API key**: Make sure to set the `API_KEY` variable in the `config.py` file to your desired API key.


## Thanks

Special Thanks

This project wouldn't have been possible without the inspiration and guidance from @rzafiamy! His expertise and kindness made a huge difference, and I'm grateful for his contributions. 🙏💖