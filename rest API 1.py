import requests
import json

response = requests.get("https://api.restful-api.dev/objects")
data1 = response.json()
#print(data1)
print('log : ', json.dumps(data1,indent = 4))
for i in data1:
    print(i["name"])
    print(i.get("data", 0))