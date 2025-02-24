# Ollama Proxy Service

### 🚨 Secure Your Data with Ease!

This repository showcases how to protect your Ollama instance using Flask, Flask-Limiter, and Flask-Cors. With this setup, you can ensure robust API key security and safeguard your valuable data.

This application uses GUNICORN as the WSGI server, providing a robust and scalable environment for running your Ollama service.

### Features

- **🔑 API Key Protection with Flask**: Ensure only authorized access by requiring a valid API key for each request.
- **🚦 Rate Limiting with Flask-Limiter**: Prevent abuse and ensure fair usage by limiting the number of API requests from a user within a specific time frame.
- **🌍 Cross-Origin Resource Sharing (CORS) with Flask-Cors**: Enable your API to be called safely from different domains, facilitating modern web application interactions.
- **📊 Systematic Logging**: Capture detailed operational data for debugging, monitoring, and security analysis.
- **🔄 Systemd Integration for Service Management**: Manage your API service effectively with capabilities like automatic restarts and dependency management.
- **🔒 Environment and Dependency Isolation with Virtual Environments**: Run your application within a controlled environment to prevent conflicts and ensure consistency.
- **⚙️ Automated Setup and Deployment Scripts**: Simplify the setup process and manage your application more efficiently with automation scripts.
- **🛡️ Secure Configuration Management**: Protect sensitive configuration settings from exposure and manage them securely.
- **🌐 Realtime Monitoring**: Monitor your API's performance in real-time to detect issues early. 

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

    By default this will start a GUNICORN server on port 11433 with 4 workers after installing the dependencies. It is the eastest way to start the service for testing purposes.

    This launcher supports different parameters:

    ```bash
    ./tools/run.sh [VENV_PATH] [WORKING_DIRECTORY] PORT=XXXX WORKERS=XX
    ```

    - `VENV_PATH`: Path to your virtual environment.
    - `WORKING_DIRECTORY`: Path to your working directory.
    - `PORT`: Port number for the GUNICORN server.
    - `WORKERS`: Number of workers for the GUNICORN server.

3. Set up SYSTEMD service using the `setup.sh` script:
    
    ```bash
    chmod +x tools/setup.sh
    ./tools/setup.sh {install|uninstall} [USERNAME] [GROUP] [WORKING_DIRECTORY] [VENV_PATH] PORT=XXXX

    ```

    - `install`: Install the service.
    - `uninstall`: Uninstall the service.
    - `{USERNAME}`: The username under which the service will run.
    - `{GROUP}`: The group under which the service will run.
    - `{WORKING_DIRECTORY}`: The directory where your application files are located.
    - `{VENV_PATH}`: The path to your virtual environment.
    - `PORT`: The port number for the GUNICORN server (default is 11433).

    This will create necessary user and group for the service, and configure the systemd service to manage the application.

4. Initialize environment files:

    ```bash
    cp .env.example .env
    cp config.example.yaml config.yaml
    ```
   
   - `.env.example`: A template for setting API keys environment variables.
   - `config.example.yaml`: A template for setting configuration parameters and LLM providers.
    

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

## Add more LLM provider 
-------------------
To add more LLM providers, you need to copy the `config.example.yaml` to `config.yaml` file. 
You need to add a new line for each LLM provider and specify the corresponding API key in `.env` file:

```bash
llm_providers:
  openai:
    base_url: "https://api.openai.com"
    headers:
      Content-Type: "application/json"

  groq:
    base_url: "https://api.groq.com/openai"
    headers:
      Content-Type: "application/json"

  ollama:
    base_url: "http://localhost:11434"
    headers:
      Content-Type: "application/json"

  cerebras:
    base_url: "https://api.cerebras.ai"
    headers:
      Content-Type: "application/json"

  deepseek:
    base_url: "https://api.deepseek.com"
    headers:
      Content-Type: "application/json"

  openrouter:
    base_url: "https://openrouter.ai/api"
    headers:
      Content-Type: "application/json"
```

Ensure that only requests with a valid API key can access Ollama.


## Port Usage
-------------------
By default, the proxy service listens on port 11433. You can change this by modifying the `default_port` in the `config.yaml` file.

In addition to that, you may have to update this also in `run.sh` and `setup.sh`.


## Rate Limit
-------------------
The proxy service has a rate limit of 100 requests per minute. You can change this by modifying the `rate_limit` in the `config.yaml` file.

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

### How to Display monitoring data in CLI

`cli.py` utility can be used to display monitoring data in CLI:

```bash
(.pyenv) python cli.py --show

+---------------------+---------------------+----------+---------------------+---------+
| Timestamp           | Endpoint            | Provider | User Email          | User ID |
+---------------------+---------------------+----------+---------------------+---------+
| 2025-02-24 22:00:07 | v1/chat/completions | groq     | unknown@example.com | unknown |
+---------------------+---------------------+----------+---------------------+---------+

```

## Troubleshooting
--------------

*   **Error streaming response**: Verify that the target URL is responding properly and that there are no network issues.
*   **Invalid API key**: Confirm that the `PROXY_API_KEY` variable in `.env` is set correctly.

## Thanks

Special Thanks

This project wouldn't have been possible without the inspiration and guidance from @rzafiamy! His expertise and kindness made a huge difference, and I'm grateful for his contributions. 🙏💖