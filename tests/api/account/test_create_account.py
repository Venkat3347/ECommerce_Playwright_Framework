from api.api_client import APIClient
import time

def test_create_account():

    payload = {
        "name": "Swamy",
        "email": f"swamy{int(time.time())}@gmail.com",
        "password": "Test@123",
        "title": "Mr",
        "birth_date": "10",
        "birth_month": "May",
        "birth_year": "1995",
        "firstname": "Swamy",
        "lastname": "Vardhineni",
        "company": "UST",
        "address1": "Madhapur",
        "address2": "Hyderabad",
        "country": "India",
        "zipcode": "500081",
        "state": "Telangana",
        "city": "Hyderabad",
        "mobile_number": "9876543210"
    }

    response = APIClient.post("/api/createAccount", payload)

    print("Status Code:", response.status_code)
    print("Response:", response.json())
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["responseCode"] == 201
    assert response_json["message"] == "User created!"