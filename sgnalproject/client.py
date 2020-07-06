import requests

""" Created to access and fetch or perform some activity in browsable web api"""

ENDPOINT = 'http://127.0.0.1:8000/api/student/'
response = requests.get(ENDPOINT)
print(response.json())