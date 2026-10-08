from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


# def test_tanpa_key_ditolak():
#     # artinya , saya mau test endpoint "v1/ask" dengan method post. harapannya reponse nya adalah {"pertanyaan": "halo dunia"}
#     # atau response-nya adalah 401 
#     resp = client.post(
#         "/v1/ask",
#         json={"pertanyaan": "halo dunia"},
#     )

#     assert resp.status_code == 401


def test_health():
    # artinya , saya mau test endpoint "v1/health" dengan method get. harapannya reponse nya adalah {"status": "ok"}
    # atau response-nya adalah 401 
    resp = client.get("/health")

    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"
