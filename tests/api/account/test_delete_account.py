from api.api_client import APIClient
from utilities.random_generator import get_test_user_for_deletion
def test_delete_account():

    # Create random user
    user = get_test_user_for_deletion()
    # Create account
    create_response = APIClient.post("/api/createAccount",user)
    print("Create Response:")
    print(create_response.json())

    assert create_response.status_code == 200
    assert create_response.json()["responseCode"] == 201

    # Delete same account
    delete_payload = {"email": user["email"],"password": user["password"]}

    delete_response = APIClient.delete("/api/deleteAccount",delete_payload)

    print("Delete Response:")
    print(delete_response.json())

    assert delete_response.status_code == 200
    delete_json = delete_response.json()
    assert delete_json["responseCode"] == 200
    assert delete_json["message"] == "Account deleted!"