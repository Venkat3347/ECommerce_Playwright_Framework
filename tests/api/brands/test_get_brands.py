from api.api_client import APIClient
import requests
import json

def test_get_all_brands():
    response = APIClient.get("/api/brandsList")

    # Validate status code
    assert response.status_code == 200
    # Convert response to JSON
    response_json = response.json()
    # Validate response contains brands
    assert "brands" in response_json
    # Validate products list is not empty
    assert len(response_json["brands"]) > 0

    print(f"Total Brands: {len(response_json['brands'])}")
    print(f"Status Code: {response.status_code}")
    print(f"Response Time: {response.elapsed.total_seconds()} seconds")
    print(json.dumps(response.json(), indent=4))