import requests

flask_server_url = 'http://http://192.168.68.116:5001' 

response = requests.get(flask_server_url)
print(response)