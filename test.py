import requests
import json
url = "http://3.87.126.120:7000/response?question="
payload = url + "hi"
response = requests.get(payload)
print(str(response.__dict__['_content'].decode("utf-8")))
response = json.loads(str(response.__dict__['_content'].decode("utf-8")))
print(response['answer'], response['score'])
