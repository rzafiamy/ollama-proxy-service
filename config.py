# config.py

API_KEY = "your_api_key_for_proxy"

DEFAULT_RATE_LIMIT = "1000 per hour"
RATE_LIMIT = "100 per minute"

LLM_PROVIDERS = {
    "openai": {
        "api_key": "your_openai_api_key",
        "base_url": "https://api.openai.com/v1",
        "headers": {"Content-Type": "application/json"}
    },
    "groq": {
        "api_key": "your_groq_api_key",
        "base_url": "https://api.groq.com/openai/v1",
        "headers": {"Content-Type": "application/json"}
    },
    "ollama": {
        "api_key": None,  # Ollama might not require an API key
        "base_url": "http://localhost:11434",
        "headers": {"Content-Type": "application/json"}
    },
    "cerebras": {
        "api_key": "your_cerebras_api_key",
        "base_url": "https://api.cerebras.ai/v1",
        "headers": {"Content-Type": "application/json"}
    },
    "deepseek": {
        "api_key": "your_deepseek_api_key",
        "base_url": "https://api.deepseek.com",
        "headers": {"Content-Type": "application/json"}
    },
    "openrouter": {
        "api_key": "your_openrouter_api_key",
        "base_url": "https://openrouter.ai/api/v1",
        "headers": {"Content-Type": "application/json"}
    }
}