from api.api_client import APIClient

def test_login_without_email():

    payload = {"password": "Password123"}
    response = APIClient.post("/api/verifyLogin", payload)
    print(response.status_code)
    print(response.text)
    print(response.json())
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["responseCode"] == 400
    assert response_json["message"] == "Bad request, email or password parameter is missing in POST request."