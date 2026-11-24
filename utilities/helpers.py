import time

def get_login_payload():
    return {
        "email": f"swamy{int(time.time())}@mail.com",
        "password": "Password123"
    }