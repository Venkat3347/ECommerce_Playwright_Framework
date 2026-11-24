import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
BASE_URL = "https://automationexercise.com"
class APIClient:

    @staticmethod
    def get(endpoint, params=None):
        return requests.get(f"{BASE_URL}{endpoint}",verify=False,params=params)
        

    @staticmethod
    def post(endpoint, payload):
        return requests.post(f"{BASE_URL}{endpoint}",data=payload,verify=False)

    @staticmethod
    def delete(endpoint, payload):
        return requests.delete(f"{BASE_URL}{endpoint}",data=payload,verify=False)

    @staticmethod
    def put(endpoint, payload):
        return requests.put(f"{BASE_URL}{endpoint}",data=payload,verify=False)