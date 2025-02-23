import os
import yaml
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Set configuration variables
API_KEY = os.getenv("PROXY_API_KEY")

# Load configuration from config.yaml
CONFIG_FILE = "config.yaml"

if not os.path.exists(CONFIG_FILE):
    raise FileNotFoundError(f"Configuration file {CONFIG_FILE} not found. Please create it from config.yaml.example.")

with open(CONFIG_FILE, "r") as f:
    config_data = yaml.safe_load(f)

# Set configuration variables
LOG_LEVEL = config_data.get("log_level", "debug")
DEFAULT_PORT = config_data.get("default_port", 11433)
DEFAULT_RATE_LIMIT = config_data.get("default_rate_limit", "1000 per hour")
RATE_LIMIT = config_data.get("rate_limit", "100 per minute")


# Load LLM Providers
LLM_PROVIDERS = config_data.get("llm_providers", {})

# Ensure API keys from environment variables override yaml values
for provider, details in LLM_PROVIDERS.items():
    env_api_key = os.getenv(f"{provider.upper()}_API_KEY")
    if env_api_key:
        details["api_key"] = env_api_key
    else:
        details["api_key"] = None
