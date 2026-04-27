import requests

data = requests.get("http://127.0.0.1:5000/api/students").json()

print("📱 Student App Data")
for d in data:
    print(d)