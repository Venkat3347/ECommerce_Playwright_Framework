from api.api_client import APIClient

def test_brands_list_put_method_not_supported():

    response = APIClient.put("/api/brandsList",{})
    print(response.json())
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["responseCode"] == 405
    assert response_json["message"] == "This request method is not supported."