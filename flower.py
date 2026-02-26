import json
import requests

url = "https://www.img2go.com/assets/dist/sample-files/img/convert_to_jpg.png"

response = requests.get(url)

data = response.json()

search_image = input("Enter the image name:")

for img in data["images"]:
    if img["name"] == search_image:
        print("Image url:",img["url"])
