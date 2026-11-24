#api/payloads.py
from api.api_client import APIClient

UPDATE_ACCOUNT_PAYLOAD = {
    "name": "Swamy Updated",
    "email": "og@gmail.com",
    "password": "OG123",
    "title": "Mr",
    "birth_date": "10",
    "birth_month": "May",
    "birth_year": "1995",
    "firstname": "Swamy",
    "lastname": "V",
    "company": "UST",
    "address1": "Hyderabad",
    "country": "India",
    "zipcode": "500081",
    "state": "Telangana",
    "city": "Hyderabad",
    "mobile_number": "9876543210"
}

response = APIClient.put(
    "/api/updateAccount",
    UPDATE_ACCOUNT_PAYLOAD
)