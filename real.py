import requests
import json

response = requests.get("https://preetkumar9054-glitch.github.io/jsondata/data.json")
data = response.json()

print(data)