import requests

url = "http://127.0.0.1:44822/"

response = requests.get(f"{url}/init")
data = response.json()
bot_id = data["bot_id"]

data = {"bot_id": bot_id, "action": 'step'}
response = requests.post(f"{url}/action", data=data)


# print(response.status_code, response.text)
print(response.status_code)

# data = json.loads(response.text)
data = response.json()

if "map" in data:
    for row in data["map"]:
        for column in row:
            if column["field"] == 4:
                print(column)
    del data["map"]
if "game" in data:
    del data["game"]
print(data)
