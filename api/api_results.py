import requests

response = requests.get(
    "https://automationexercise.com/api/productsList",
    verify=False
)

print(response.status_code)
print(response.text)