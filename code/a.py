import json
with open("stuff.json", encoding="utf-8") as f:
    stuff = json.load(f)

for i in stuff["result"]:
    print(i)