from api.api_client import APIClient

def test_search_product_without_parameter():
    response = APIClient.post("/api/searchProduct",{})
    print(response.json())
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["responseCode"] == 400
    assert response_json["message"] == "Bad request, search_product parameter is missing in POST request."