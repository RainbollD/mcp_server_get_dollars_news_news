import pytest
from main import server


# Декоратор для создания фикстуры
@pytest.fixture()
def client():
    with server.test_client() as client:
        yield client

# Проверка маршрута /rate
def test_rate(client):
    response = client.get('/rate')
    assert response.status_code == 200

# Проверка маршрута /weather
def test_weather(client):
    response = client.get('/weather/Moscow')
    assert response.status_code == 200

# Проверка маршрута /news
def test_news(client):
    response = client.get('/news')
    assert response.status_code == 200
