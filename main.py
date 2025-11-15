import requests

url = "http://127.0.0.1:1337/ask"
payload = {
    "message": "Hey Marta, what are you wearing?",
    "model": "gosh-v2-"
}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)
print(response.json())
print("to getit contact Tg: @PatchLoop")
