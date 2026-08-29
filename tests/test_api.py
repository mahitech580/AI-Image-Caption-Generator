from app import app

def test_home():
    client = app.test_client(); response = client.get("/"); assert response.status_code == 200

def test_health():
    client = app.test_client(); response = client.get("/api/health"); assert response.status_code == 200; data = response.get_json(); assert data["success"] is True; assert data["status"] == "healthy"

def test_caption_without_image():
    client = app.test_client(); response = client.post("/api/caption"); assert response.status_code == 400; assert response.get_json()["success"] is False
