[Unit]
Description=Ollama Proxy Flask App
After=network.target

[Service]
User={{USERNAME}}
Group={{GROUP}}
WorkingDirectory={{WORKING_DIRECTORY}}
Environment="PATH={{VENV_PATH}}/bin"
ExecStart={{WORKING_DIRECTORY}}/tools/run.sh
StandardOutput=append:/var/log/ollama_proxy_app.log
StandardError=append:/var/log/ollama_proxy_app_error.log
Restart=always

[Install]
WantedBy=multi-user.target