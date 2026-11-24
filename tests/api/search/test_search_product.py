from api.api_client import APIClient

def test_search_product():
    payload = {"search_product": "Blue Top"}
    response = APIClient.post("/api/searchProduct",payload)
    print("Status Code:", response.status_code)
    print("Response:", response.json())

    assert response.status_code == 200
    response_json = response.json()
    assert "products" in response_json
    #assert len(response_json["products"]) > 0
    assert response_json["products"][0]["name"] == "Blue Top"