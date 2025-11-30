from app import app

def test_vacunas_status():
    client = app.test_client()
    resp = client.get("/vacunas")
    assert resp.status_code == 200

def test_vacunas_por_ano_status():
    client = app.test_client()
    resp = client.get("/vacunas/2001")
    assert resp.status_code == 200
