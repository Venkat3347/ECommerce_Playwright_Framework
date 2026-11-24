from api.api_client import APIClient

def test_login_without_password():
    payload = {"email": "test@gmail.com"}
    response = APIClient.post("/api/verifyLogin",payload)
    print(response.json())
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["responseCode"] == 400
    assert response_json["message"] == "Bad request, email or password parameter is missing in POST request."