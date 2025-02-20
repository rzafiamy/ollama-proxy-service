from flask import Flask, request, jsonify, abort, Response
import requests
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_cors import CORS
import config

app = Flask(__name__)
CORS(app)

limiter = Limiter(
    key_func=get_remote_address,
    app=app,
    default_limits=[config.DEFAULT_RATE_LIMIT]
)

def require_api_key(view_function):
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            abort(401)
        token = auth_header[7:]
        if token != config.API_KEY:
            abort(401)
        return view_function(*args, **kwargs)
    return decorated_function

@app.route('/proxy/<provider>/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@require_api_key
@limiter.limit(config.RATE_LIMIT)
def proxy(provider, path):
    """Proxy requests to different LLM providers."""
    if provider not in config.LLM_PROVIDERS:
        return jsonify({"error": "Invalid provider"}), 400

    provider_info = config.LLM_PROVIDERS[provider]
    url = f"{provider_info['base_url']}/{path}"

    headers = {key: value for key, value in request.headers if key.lower() != 'host'}
    if provider_info["api_key"]:
        headers["Authorization"] = f"Bearer {provider_info['api_key']}"  # Add API key if required

    req = requests.Request(request.method, url, headers=headers, 
                           json=request.json, params=request.args, data=request.get_data())
    prepared_req = req.prepare()
    
    session = requests.Session()
    resp = session.send(prepared_req, stream=True)

    def generate():
        try:
            for chunk in resp.iter_content(chunk_size=4096):
                yield chunk
        except Exception as e:
            app.logger.error(f"Error streaming response: {e}")
            raise e
        finally:
            resp.close()

    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for name, value in resp.headers.items() if name.lower() not in excluded_headers]

    return Response(generate(), status=resp.status_code, headers=headers)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=11433, debug=False)
