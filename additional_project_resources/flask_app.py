from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_request_headers():
    """
    Retrieves the incoming HTTP request headers and returns them
    as a JSON object in the response body.
    """
    request_headers = dict(request.headers)
    
    response_payload = {
        "message": "The following HTTP request headers were received:",
        "request_headers": request_headers
    }
    
    return jsonify(response_payload)

if __name__ == '__main__':
    print("🚀 Starting Flask server...")
    app.run(host='127.0.0.1', port=5000)