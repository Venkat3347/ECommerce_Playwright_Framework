from api.api_client import APIClient
#from api.payloads import UPDATE_ACCOUNT_PAYLOAD

def test_update_account():

   payload= {"name": "Swamy Updated","email": "og123@gmail.com","password": "OG123"}
   response = APIClient.put("/api/updateAccount",payload)

   print("Status Code:", response.status_code)
   print("Response:", response.text)
   print("JSON:", response.json())
   response_json = response.json()
   assert response_json["responseCode"] == 200
   assert response_json["message"] == "User updated!"
   print("Updated Name:", payload["name"])