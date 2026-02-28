import json
shipments: dict = {}
with open("Shipements.json") as json_file:
    data = json.load(json_file)
    for value in data:
        shipments[value["ID"]] = value

def save():
    with open("Shipements.json","w") as json_file:
        json.dump(list(shipments.values()),json_file)