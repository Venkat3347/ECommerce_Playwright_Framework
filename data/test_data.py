import time

def get_test_user():
   return {

    "name": "Swamy",
    "email": f"swamy{int(time.time())}@mail.com",
    "password": "Password123",
    "first_name": "Swamy",
    "last_name": "Vardhineni",
    "company": "UST",
    "address": "Hyderabad",
    "address2": "Hitech City",
    "country": "India",
    "state": "Telangana",
    "city": "Hyderabad",
    "zipcode": "500081",
    "mobile": "9876543210"
}

LOGIN_TEST_DATA = [

    ("og123@gmail.com","OG123","success"),
    ("invalid@test.com","wrong123","failure")
]

SUBSCRIPTION_EMAIL = "test123@gmail.com"