import time

def get_test_user_for_deletion():
    return {
        "name": "Swamy",
        "email": f"swamy{int(time.time())}@mail.com",
        "password": "Password123",
        "title": "Mr",
        "birth_date": "10",
        "birth_month": "May",
        "birth_year": "1995",
        "firstname": "Swamy",
        "lastname": "Vardhineni",
        "company": "UST",
        "address1": "Hyderabad",
        "address2": "Hitech City",
        "country": "India",
        "zipcode": "500081",
        "state": "Telangana",
        "city": "Hyderabad",
        "mobile_number": "9876543210"
    }