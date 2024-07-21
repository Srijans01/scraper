import requests

url = "http://127.0.0.1:8000/scrape"
headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
    "x-token": "srijan"
}
data = {
    "num_pages": 5,
    "proxy": None
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
