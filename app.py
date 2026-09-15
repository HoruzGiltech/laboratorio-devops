import os
from flask import Flask, jsonify

app = Flask(__name__)

# Lista global para retener la memoria y evitar que el garbage collector la libere
memory_hog = []

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

@app.route('/memory-leak')
def memory_leak():
    # Asigna aproximadamente 30MB extra en cada petición
    dummy_data = 'X' * (30 * 1024 * 1024)
    memory_hog.append(dummy_data)
    return jsonify({
        "status": "leaking",
        "allocated_blocks": len(memory_hog),
        "message": "Consumiendo 30MB adicionales de memoria RAM... 🧠💥"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)