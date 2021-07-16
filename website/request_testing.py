import requests

BASE_URL = "https://4fd8ef0e3912.ngrok.io"

data1 = {
  "name": "Golden Retriever in a flower crown",
  "url": "1",
  "views": 1
  }

data2 = {
  "name": "Hello There",
  "url": "2",
  "views": 100000000000
  }

output = requests.post(f"{BASE_URL}/image/1", data=data1)
print("Image one created")
output = requests.post(f"{BASE_URL}/image/2", data=data2)
print("Image two created")
output = requests.get(f"{BASE_URL}/image/2")
print(output.json())
output = requests.get(f"{BASE_URL}/image/1")
print(output.json())
output = requests.put(f"{BASE_URL}/image/1", {"views": 5})
print(output.json())
output = requests.get(f"{BASE_URL}/image/1")
print(output.json())
output = requests.get(f"{BASE_URL}/image/2")
print(output.json())

output = requests.get(f"{BASE_URL}/dummy")
print(output.json())

requests.delete(f"{BASE_URL}/image/")