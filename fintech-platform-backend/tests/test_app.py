from fastapi.testclient import TestClient
from fintech_platform_backend.app import app
from http import HTTPStatus

def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app=app)
    response = client.get('/api')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello, World!'}
