# Ollama Proxy Service

### 🚨 Secure Your Data with Ease!

This repository showcases how to protect your Ollama instance using Flask, Flask-Limiter, and Flask-Cors. With this setup, you can ensure robust API key security and safeguard your valuable data.

### Features

- **🔑 API Key Protection with Flask**: Ensure only authorized access by requiring a valid API key for each request.
- **🚦 Rate Limiting with Flask-Limiter**: Prevent abuse and ensure fair usage by limiting the number of API requests from a user within a specific time frame.
- **🌍 Cross-Origin Resource Sharing (CORS) with Flask-Cors**: Enable your API to be called safely from different domains, facilitating modern web application interactions.
- **📊 Systematic Logging**: Capture detailed operational data for debugging, monitoring, and security analysis.
- **🔄 Systemd Integration for Service Management**: Manage your API service effectively with capabilities like automatic restarts and dependency management.
- **🔒 Environment and Dependency Isolation with Virtual Environments**: Run your application within a controlled environment to prevent conflicts and ensure consistency.
- **⚙️ Automated Setup and Deployment Scripts**: Simplify the setup process and manage your application more efficiently with automation scripts.
- **🛡️ Secure Configuration Management**: Protect sensitive configuration settings from exposure and manage them securely.


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
    git clone https://github.com/rzafiamy/ollama-proxy-service
    cd ollama-proxy-service
    ```

2. Install the required dependencies:

    For this, you can run your script once as below:

    ```bash
    chmod +x tools/run.sh
    ./tools/run.sh
    ```

3. Set up the service using the setup script:
    ```bash
    chmod +x tools/setup.sh
    ./tools/setup.sh install
    ```

4. Initialize the `.env` file:

    ```bash
    cp .env.example .env
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
./tools/run.sh
```

This will ensure the virtual environment is set up and start the Flask application on the default port 11433. Access it by visiting `http://localhost:11433` in your browser.

### API Key

To protect Ollama proxy with an API key, set the `PROXY_API_KEY` variable in your `.env` file. This is the API key that you have to use to authenticate your requests. This is crucial for security reasons, as it prevents unauthorized access to the LLM services. The remaining API keys are needed if you want to use another LLM provider. For this, you have to generate them from your provider account.

```python
# .env file (DO NOT COMMIT THIS FILE)

PROXY_API_KEY="your_proxy_api_key"

OPENAI_API_KEY="your_openai_api_key"
GROQ_API_KEY="your_groq_api_key"
CEREBRAS_API_KEY="your_cerebras_api_key"
DEEPSEEK_API_KEY="your_deepseek_api_key"
OPENROUTER_API_KEY="your_openrouter_api_key"
```

Ensure that only requests with a valid API key can access Ollama.

## Update ollama and keep environment

```bash
chmod +x tools/ollama_update.sh
bash tools/ollama_update.sh
```

## API Documentation
-------------------

### API Endpoints

The proxy service supports all standard HTTP methods (GET and POST) and has one endpoint `/` that proxies requests to the target URL depending on the requested provider.

### Examples

#### SEND Request to OpenAI API

```bash
    curl -X POST https://api.myserver.ltd/proxy/openai/v1/completions \
        -H "Authorization: Bearer PROXY_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{"prompt": "Hello world", "max_tokens": 5, "model": "gpt-3.5"}'
```

#### SEND Request to Cerebras API

```bash
    curl -X POST https://api.myserver.ltd/proxy/cerebras/v1/completions \
        -H "Authorization: Bearer PROXY_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{"prompt": "Hello world", "max_tokens": 5, "model": "llama-3.3-70b"}'
```

#### GET list of models available in Groq API

```bash
    curl -X GET https://api.myserver.ltd/proxy/groq/v1/models \
        -H "Authorization: Bearer PROXY_API_KEY" \
        -H "Content-Type: application/json"
```

### How to Use it in Open-webUI

Use the following URL in Open-webUI configuration and paste the PROXY_API_KEY:

```bash
   https://myserver.ltd/proxy/<provider>/v1
```

## Troubleshooting
--------------

*   **Error streaming response**: Verify that the target URL is responding properly and that there are no network issues.
*   **Invalid API key**: Confirm that the `PROXY_API_KEY` variable in `.env` is set correctly.

## Thanks

Special Thanks

This project wouldn't have been possible without the inspiration and guidance from @rzafiamy! His expertise and kindness made a huge difference, and I'm grateful for his contributions. 🙏💖