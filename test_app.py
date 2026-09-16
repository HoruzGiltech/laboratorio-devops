import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'ok'
    assert data['message'] == '¡Hola desde Kubernetes con CI/CD automatico en GCP! 🚀'
    assert data['version'] == '2.0.0'

def test_healthz(client):
    response = client.get('/healthz')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'
    assert data['message'] == 'La aplicacion esta funcionando correctamente... ✅'