from api.api_client import APIClient

def test_verify_login():
    payload = {"email": "OG@gmail.com", "password": "OG123"}
    response = APIClient.post("/api/verifyLogin",payload)
    print("Status Code:", response.status_code)
    print("Response:", response.json())

    assert response.status_code == 200
    response_json = response.json()
    assert response_json["responseCode"] == 200
    assert response_json["message"] == "User exists!"