from api.api_client import APIClient

def test_login_invalid_credentials():
    payload = {"email": "invalid@gmail.com","password": "wrongpassword"}
    response = APIClient.post("/api/verifyLogin",payload)

    print(response.json())
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["responseCode"] == 404
    assert response_json["message"] == "User not found!"