import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "ok",
        "message": "¡Hola desde Kubernetes con CI/CD automatico en GCP! 🚀",
        "version": "2.0.0"
    })

@app.route('/crash')
def crash():
    os._exit(1)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
