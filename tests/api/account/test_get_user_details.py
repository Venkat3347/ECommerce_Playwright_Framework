from api.api_client import APIClient

def test_get_user_details_by_email():

    email = "OG@gmail.com"
    response = APIClient.get("/api/getUserDetailByEmail",params={"email": email})
    print(response.text)
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["responseCode"] == 200
    assert response_json["user"]["email"] == email
    print("Response:", response.json())