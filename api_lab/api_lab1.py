import requests     # run cmd to install request => python -m pip install requests

response = requests.get(
    "https://api.github.com",
    timeout=10
)

print("Status Code:", response.status_code)
print("Content-Type:", 
      response.headers["Content-Type"])
print("Response Body:")
print(response.text)

