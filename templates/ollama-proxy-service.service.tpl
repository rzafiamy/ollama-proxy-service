[Unit]
Description=Ollama Proxy Flask App
After=network.target

[Service]
User={{USERNAME}}
Group={{GROUP}}
WorkingDirectory={{WORKING_DIRECTORY}}
Environment="PATH={{VENV_PATH}}"
ExecStart={{VENV_PATH}}/bin/gunicorn -w 4 -b 0.0.0.0:{{PORT}} app:app

# Log configuration
StandardOutput=file:/var/log/ollama_proxy_app.log
StandardError=file:/var/log/ollama_proxy_app_error.log

Restart=always

[Install]
WantedBy=multi-user.target