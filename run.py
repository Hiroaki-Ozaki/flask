import requests
import json
import sys

PATH = ' '.join(sys.argv[1:])

# Replace ◯◯◯◯◯ with local server address
URL = "http://◯◯◯◯◯/api/predict"
DATA = {"image_path": PATH}

# Send JSON to local server
response = requests.post(URL, json=DATA)
print(response.text)

# Convert the returned JSON to dictionary type
result = json.loads(response.text)
print(result["prediction"])

# Judge dogs and cats
if result["prediction"] < 0.5:
    print("This is cat")
if result["prediction"] > 0.5:
    print("This is dog")