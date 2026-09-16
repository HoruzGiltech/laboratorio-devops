import os
import time
from flask import Flask, jsonify

app = Flask(__name__)

# Lista global para retener la memoria y evitar que el garbage collector la libere
memory_hog = []
is_healthy = True

@app.route('/')
def home():
    return jsonify({
        "status": "ok",
        "message": "¡Hola desde Kubernetes con CI/CD automatico en GCP! con nuevas funcionalidades 🚀",
        "version": "3.0.0"
    })

@app.route('/healthz')
def healthz():
    if is_healthy:
        return jsonify({
            "status": "healthy",
            "message": "La aplicacion esta funcionando correctamente... ✅"
        }), 200
    else:
        return jsonify({
            "status": "unhealthy",
            "message": "La aplicacion ha entrado en un estado de bloqueo interno... ❄️"
        }), 500


@app.route ('/freeze')
def freeze():
    global is_healthy
    is_healthy = False
    return jsonify({
        "status": "frozen",
        "message": "La aplicacion ha entrado en un estado de bloqueo interno... ❄️"
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