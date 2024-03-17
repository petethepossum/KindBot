import requests
from bs4 import BeautifulSoup

flask_server_url = 'http://172.20.10.8:5001'

# Send request to Flask server to get input text
response = requests.get(flask_server_url)

if response.status_code == 200:
    # Parse HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    # Extract text content
    text_content = soup.get_text()
    print("Received text from server:")
    print(text_content)
else:
    print("Failed to get text from server")