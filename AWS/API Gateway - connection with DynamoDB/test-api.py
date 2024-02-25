import requests
import json

my_data = json.dumps({"postID": "5","text": "some sample text"})
headers = {'Content-Type': 'application/json'}
r = requests.post('https://4akeo75k98.execute-api.eu-central-1.amazonaws.com/posts', data = my_data, headers = headers)
print(r.json())