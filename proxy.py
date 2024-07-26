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
    default_limits=["100 per hour"]
)


def require_api_key(view_function):
    def decorated_function(*args, **kwargs):
        # Extract the token from the Authorization header
        auth_header = request.headers.get('Authorization')
        print(request.headers)
        if not auth_header or not auth_header.startswith('Bearer '):
            abort(401)  # Unauthorized access if no or improperly formatted token
        token = auth_header[7:]  # Remove 'Bearer ' prefix to isolate the token
        if token != config.API_KEY:
            abort(401)  # Unauthorized access if the token does not match
        return view_function(*args, **kwargs)
    return decorated_function

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@require_api_key
@limiter.limit("10 per minute")
def proxy(path):
    global TARGET_URL
    url = f"{config.TARGET_URL}/{path}"
    req = requests.Request(request.method, url, headers={key: value for (key, value) in request.headers if key != 'Host'},
                           data=request.get_data(), params=request.args, cookies=request.cookies)
    prepared_req = req.prepare()
    session = requests.Session()
    resp = session.send(prepared_req, stream=True)

    def generate():
        try:
            for chunk in resp.iter_content(chunk_size=4096):
                yield chunk
        except Exception as e:
            app.logger.error("Error streaming response: %s", e)
            raise e
        finally:
            resp.close()

    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in resp.headers.items()
               if name.lower() not in excluded_headers]

    return Response(generate(), status=resp.status_code, headers=headers)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=11433, debug=False)
