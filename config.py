# config.py
import os
from dotenv import load_dotenv

DEFAULT_RATE_LIMIT = "1000 per hour"
RATE_LIMIT = "100 per minute"


# Load environment variables from .env
load_dotenv()

API_KEY = os.getenv("PROXY_API_KEY")

LLM_PROVIDERS = {
    "openai": {
        "api_key": os.getenv("OPENAI_API_KEY"),
        "base_url": "https://api.openai.com/v1",
        "headers": {"Content-Type": "application/json"}
    },
    "groq": {
        "api_key": os.getenv("GROQ_API_KEY"),
        "base_url": "https://api.groq.com/openai/v1",
        "headers": {"Content-Type": "application/json"}
    },
    "ollama": {
        "api_key": None,  # Ollama might not require an API key
        "base_url": "http://localhost:11434",
        "headers": {"Content-Type": "application/json"}
    },
    "cerebras": {
        "api_key": os.getenv("CEREBRAS_API_KEY"),
        "base_url": "https://api.cerebras.ai/v1",
        "headers": {"Content-Type": "application/json"}
    },
    "deepseek": {
        "api_key": os.getenv("DEEPSEEK_API_KEY"),
        "base_url": "https://api.deepseek.com",
        "headers": {"Content-Type": "application/json"}
    },
    "openrouter": {
        "api_key": os.getenv("OPENROUTER_API_KEY"),
        "base_url": "https://openrouter.ai/api/v1",
        "headers": {"Content-Type": "application/json"}
    }
}
